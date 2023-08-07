import ros_api
import os
from dotenv import load_dotenv
load_dotenv()

# VARS
MIKROTIK_IP=os.getenv("MIKROTIK_IP")
API_USER=os.getenv("API_USER")
API_PASSWORD=os.getenv("API_PASSWORD")
API_PORT=os.getenv("API_PORT")

router = ros_api.Api(address=MIKROTIK_IP, user=API_USER, password=API_PASSWORD, port=API_PORT)
r = router.talk('/ip/address/print')
print(r)
