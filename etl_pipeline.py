import pandas as pd
import paramiko
import logging

# Setup logging
logging.basicConfig(filename="pipeline.log", level=logging.INFO)

# Step 1: Extract mock data
data = pd.DataFrame({
    "TransactionID": [101, 102, 103],
    "Amount": [250.00, 120.50, 89.99],
    "Status": ["Posted", "Settled", "Posted"]
})

# Step 2: Transform to CSV
data.to_csv("settlement.csv", index=False)

# Step 3: Transmit via SFTP (mock)
try:
    transport = paramiko.Transport(("localhost", 22))
    transport.connect(username="user", password="pass")
    sftp = paramiko.SFTPClient.from_transport(transport)
    sftp.put("settlement.csv", "/remote/settlement.csv")
    logging.info("File transmitted successfully.")
except Exception as e:
    logging.error(f"Transmission failed: {e}")
finally:
    transport.close()
