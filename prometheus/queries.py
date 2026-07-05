CPU_USAGE = """
sum(
    rate(
        container_cpu_usage_seconds_total{{
            pod="{pod}"
        }}[5m]
    )
)
"""

MEMORY_USAGE = """
sum(
    container_memory_working_set_bytes{{
        pod="{pod}"
    }}
)
"""

RESTART_COUNT = """
kube_pod_container_status_restarts_total{{
    pod="{pod}"
}}
"""

READY_STATUS = """
kube_pod_status_ready{{
    pod="{pod}",
    condition="true"
}}
"""

POD_PHASE = """
kube_pod_status_phase{{
    pod="{pod}"
}}
"""

NETWORK_RX = """
sum(
    rate(
        container_network_receive_bytes_total{{
            pod="{pod}"
        }}[5m]
    )
)
"""

NETWORK_TX = """
sum(
    rate(
        container_network_transmit_bytes_total{{
            pod="{pod}"
        }}[5m]
    )
)
"""
