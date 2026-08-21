# Identify transactions posted but not settled
SELECT p.TransactionID, p.Amount, p.PostingDate
FROM Posting p
LEFT JOIN Settlement s
  ON p.TransactionID = s.TransactionID
WHERE s.TransactionID IS NULL;

# Identify mismatched amounts between posting and settlement
SELECT p.TransactionID, p.Amount AS PostedAmount, s.Amount AS SettledAmount
FROM Posting p
INNER JOIN Settlement s
  ON p.TransactionID = s.TransactionID
WHERE p.Amount <> s.Amount;

## KPI: Count of mismatches
SELECT COUNT(*) AS MismatchCount
FROM Posting p
INNER JOIN Settlement s
  ON p.TransactionID = s.TransactionID
WHERE p.Amount <> s.Amount;
