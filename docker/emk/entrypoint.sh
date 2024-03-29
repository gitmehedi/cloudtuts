#!/bin/bash

set -e

# set the postgres database host, port, user and password according to the environment
# and pass them as arguments to the odoo process if not present in the config file
: ${HOST:=${DB_PORT_5432_TCP_ADDR:='db'}}
: ${PORT:=${DB_PORT_5432_TCP_PORT:=5432}}
: ${USER:=${DB_ENV_POSTGRES_USER:=${POSTGRES_USER:='odoo'}}}
: ${PASSWORD:=${DB_ENV_POSTGRES_PASSWORD:=${POSTGRES_PASSWORD:='odoo'}}}

DB_ARGS=()
function check_config() {
    param="$1"
    value="$2"
    if ! grep -q -E "^\s*\b${param}\b\s*=" "$ODOO_RC" ; then
        DB_ARGS+=("--${param}")
        DB_ARGS+=("${value}")
   fi;
}
ODOO_RC='/etc/odoo/odoo.conf'
check_config "db_host" "$HOST"
check_config "db_port" "$PORT"
check_config "db_user" "$USER"
check_config "db_password" "$PASSWORD"

chown -R odoo:odoo /var/lib/odoo/
chmod 777 -R /var/lib/odoo/

case "$1" in
    -- | odoo)
        shift
        if [[ "$1" == "scaffold" ]] ; then
            # exec odoo "$ODOO_RC" "$@" -u all
            exec odoo "$@" "${DB_ARGS[@]}"
        else
            # exec odoo "$ODOO_RC" "$@" "${DB_ARGS[@]}" -u all
            exec odoo "$@" "${DB_ARGS[@]}"
        fi
        ;;
    -*)
        # exec odoo "$@" "${DB_ARGS[@]}" -u all
        exec odoo "$@" "${DB_ARGS[@]}"
        ;;
    *)
        exec "$@"
esac

exit 1