from datetime import datetime, timedelta
import logging

logging.basicConfig(level=logging.INFO)

class Device:
    def __init__(self, device_id, device_type, owner, firmware_version="1.0.0"):
        if not isinstance(device_id, str) or not device_id:
            raise ValueError('device_id must be a non-empty string')
        if not isinstance(owner, str) or not owner:
            raise ValueError("owner must be a non-empty string")
        if device_type not in ("sensor", "actuator", "camera"):
            raise ValueError("device_type must be one of 'sensor', 'actuator', 'camera'")
        
        self.__device_id = device_id
        self.__device_type = device_type
        self.__owner_id = owner
        self.__firmware_version = firmware_version
        self.__compliance_status = "unknown"
        self.__last_security_check = None
        self.__is_active = True
        self.__access_log = []

    
    def authorize_access(self, user, action):
        self.check_compliance()  

        if not self.__is_active or self.__compliance_status != "pass":
            self.__access_log.append((user.get_username(), action, "Denied", datetime.now()))
            logging.warning(f"Access DENIED for {user.get_username()} to {action} on device {self.__device_id}")
            return False

        level = self.Administration(user)
        permissions = {
            'owner, full authorization': {'read', 'write', 'edit'},
            'employee, semi authorization': {'read', 'write'},
            'guest, default authorization': {'read'}
        }

        if action in permissions[level]:
            self.__access_log.append((user.get_username(), action, "Authorized", datetime.now()))
            logging.info(f"Access GRANTED for {user.get_username()} to {action} on device {self.__device_id}")
            return True
        else:
            self.__access_log.append((user.get_username(), action, "Denied", datetime.now()))
            logging.warning(f"Access DENIED for {user.get_username()} to {action} on device {self.__device_id}")
            return False

    def Administration(self, user):
        Level = [
            'owner, full authorization',
            'employee, semi authorization',
            'guest, default authorization'
        ]
        if user.get_username() == self.__owner_id:
            return Level[0]
        elif hasattr(user, 'role') and user.role == 'employee':
            return Level[1]
        else:
            return Level[2]

    
    def run_security_scan(self):
        self.__last_security_check = datetime.now()
        logging.info(f"Security scan completed for device {self.__device_id}")

    def update_firmware(self, new_version):
        self.__firmware_version = new_version
        logging.info(f"Firmware updated to {new_version} for device {self.__device_id}")

    def check_compliance(self):
        if self.__last_security_check:
            if datetime.now() - self.__last_security_check > timedelta(days=30):
                self.__compliance_status = "fail"
            else:
                self.__compliance_status = "pass"
        else:
            self.__compliance_status = "fail"
        return self.__compliance_status

    def quarantine(self):
        self.__is_active = False
        self.__compliance_status = "fail"
        logging.warning(f"Device {self.__device_id} has been quarantined!")

    def override_compliance(self, user, status):
        if user.get_username() == self.__owner_id:
            self.__compliance_status = status
            logging.info(f"Compliance overridden by {user.get_username()} to {status} for device {self.__device_id}")
            return True
        return False

    
    def get_device_id(self):
        return self.__device_id

    def get_device_type(self):
        return self.__device_type

    def get_firmware_version(self):
        return self.__firmware_version

    def get_compliance_status(self):
        return self.__compliance_status

    def get_availability(self):
        return "online" if self.__is_active else "offline"



class DeviceManager:
    def __init__(self):
        self.devices = []

    def add_device(self, device):
        self.devices.append(device)
        logging.info(f"Device {device.get_device_id()} added to manager")

    def remove_device(self, device_id):
        self.devices = [d for d in self.devices if d.get_device_id() != device_id]
        logging.info(f"Device {device_id} removed from manager")

    def generate_security_report(self):
        report = []
        for d in self.devices:
            
            device_id = d.get_device_id()
            device_type = d.get_device_type()
            firmware = d.get_firmware_version()
            compliance = d.get_compliance_status()
            availability = d.get_availability()

            report.append({
                "device_id": device_id,
                "device_type": device_type,
                "firmware_version": firmware,
                "compliance_status": compliance,
                "availability": availability
            })
        logging.info("Security report generated")
        return report