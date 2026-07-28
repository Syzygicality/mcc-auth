# mcc-auth

Configuration mirror of a self-hosted Keycloak instance running on an
Android/Termux device, fronted by a Cloudflare tunnel, with services supervised
by `runit`.

Paths in this repo mirror `$HOME` on the device
(`/data/data/com.termux/files/home`), so `sv/keycloak/run` here is
`~/sv/keycloak/run` there.

## What's running

| Service | Supervised by | Notes |
| --- | --- | --- |
| `keycloak` | `sv/keycloak/run` | HTTP on `:8080`, Postgres backend, behind a proxy |
| `postgres` | `sv/postgres/run` | data dir `$PREFIX/var/lib/postgresql`, db/role `keycloak` |
| `cloudflared` | `sv/cloudflared/run` | named tunnel → `localhost:8080` |
| `sshd` | `sv/sshd/run` | remote administration |

Boot path: Termux:Boot runs `.termux/boot/start.sh`, which calls `scripts/stop.sh`
to clear stale processes, takes a wake lock, then starts `runsvdir ~/sv`.

## Configuration

Environment-specific and sensitive values are not committed. Copy
`secrets.env.example` to `~/secrets.env` on the device and fill it in;
`sv/keycloak/run` sources it and exports the variables that
`keycloak/conf/keycloak.conf` expands (`${KC_DB_PASSWORD}`, `${KC_HOSTNAME}`).

`.cloudflared/config.yml` uses `<TUNNEL_ID>` and `<PUBLIC_HOSTNAME>` placeholders —
substitute the real values in the copy that lives on the device.

Note that `sv/keycloak/run` intentionally differs from the deployed copy: this
version sources `~/secrets.env` rather than defining credentials inline.

## What is not mirrored

The device's `$HOME` is ~2.7 GB; this repo holds only configuration.

- **Credentials** — the Cloudflare tunnel credentials file and origin certificate,
  and all values in `~/secrets.env`.
- **`.ssh/`** — keys, `authorized_keys`, and client config. Access-control and
  network-topology state; not needed to reconstruct the service stack.
- **Vendored binaries** — the Keycloak distribution (`bin/`, `lib/`, `data/`,
  ~171 MB) and its stock docs. Only `conf/` is kept.
- **Caches** — `.cargo`, `.cache`, `.vscode-server` (~2.5 GB combined).
- **Runtime state** — `logs/` and every `sv/*/supervise/` directory (pids, locks,
  status files); `runit` regenerates these.
- **Shell and tool history** — `.bash_history`, `.psql_history`, `.viminfo`,
  `.wget-hsts`, `.termux_authinfo`.

See `.gitignore` for the enforced exclusions.
