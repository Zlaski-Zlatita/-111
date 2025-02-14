
WITH FreshBalances as ( 
  SELECT A.ID AS ACCOUNT_ID, SUM(CASE WHEN R.DT = 1 THEN -R.SUM ELSE R.SUM END) as ActualBalance
  FROM ACCOUNTS A
  JOIN RECORDS R ON R.ACC_REF = A.ID 
  GROUP BY A.ID
) 
UPDATE ACCOUNTS A
SET SALDO = F.ActualBalance
FROM FreshBalances F
WHERE A.ID = F.ACCOUNT_ID AND A.SALDO != F.ActualBalance;


