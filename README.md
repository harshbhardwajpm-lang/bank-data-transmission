# bank-data-transmission
Automating daily/weekly/monthly posting and settlement data feeds to banks via Visa NDM or SFTP.

# Objective
Simulate posting and settlement data transmission from DES systems to banks via secure channels (Visa NDM / SFTP).

# Workflow
1. Extract posting & settlement data (mock dataset).
2. Transform into required format (CSV).
3. Transmit securely to a mock SFTP server.
4. Log success/failure and generate compliance audit trail.

# Tech Stack
- Python (ETL scripts)
- SQL (reconciliation queries)
- Paramiko (SFTP simulation)
- Logging module for error handling

# KPIs
- Transmission success rate
- Error reduction %
- SLA adherence

# Business Impact
Ensures secure, timely delivery of settlement data to banks, reducing reconciliation errors and improving compliance.
