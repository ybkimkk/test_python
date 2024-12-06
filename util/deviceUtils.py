import platform
import uuid


def get_machine_code():
    try:
        mac = uuid.getnode()
        os_name = platform.system()
        cpu_info = platform.processor()

        unique_code = f"{os_name}-{mac}-{cpu_info.replace(',', '')}"
        return unique_code
    except Exception as e:
        return f"Error: {e}"