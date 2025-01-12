SELECT A.*
FROM ACCOUNTS A
  JOIN PRODUCTS P ON A.PRODUCT_REF = P.ID
WHERE P.PRODUCT_TYPE_ID = (SELECT ID FROM PRODUCT_TYPE WHERE NAME = 'ДЕПОЗИТ') AND P.CLIENT_REF NOT IN (
  SELECT CLIENT_REF FROM PRODUCTS
  WHERE PRODUCT_TYPE_ID = (SELECT ID FROM PRODUCT_TYPE WHERE NAME = 'КРЕДИТ')
);

SELECT PT.NAME AS PRODUCT_TYPE,
   AVG(case when R.DT = 1 then -R.SUM else R.SUM end) AS AVG_MOVEMENT
FROM RECORDS R
JOIN ACCOUNTS A ON R.ACC_REF = A.ID
JOIN PRODUCTS P ON A.PRODUCT_REF = P.ID
JOIN PRODUCT_TYPE PT ON P.PRODUCT_TYPE_ID = PT.ID
GROUP BY PT.NAME;

SELECT C.NAME AS CLIENT_NAME,
   R.OPER_DATE,
   SUM(CASE WHEN R.DT = 1 THEN -R.SUM ELSE R.SUM END) AS TOTAL_SUM
FROM RESCORDS R
JOIN ACCOUNTS A ON R.ACC_REF = A.ID
JOIN PRODUCTS P ON A.PRODUCT_REF = P.ID
JOIN CLIENTS C ON P.CLIENT_REF = C.ID
WHERE R.OPER_DATE >= NOW() - INTERVAL '1 month'
GROUP BY CLIENT_NAME, R.OPER_DATE;

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

SELECT DISTINCT C.*
FROM CLIENTS C
  JOIN PRODUCTS P ON C.ID = P.CLIENT_REF
WHERE P.PRODUCT_TYPE_ID = (SELECT ID FROM PRODUCT_TYPE WHERE NAME = 'КРЕДИТ')
AND NOT EXISTS (
  SELECT 1
  FROM RECORDS R
  JOIN ACCOUNTS A ON R.ACC_REF = A.ID
  WHERE A.PRODUCT_REF = P.ID AND R.DT = 1
  GROUP BY A.ID
  HAVING SUM(R.SUM) < (SELECT MAX(R2.SUM) FROM RECORDS R2 JOIN ACCOUNTS A2 ON R2.ACC_REF = A2.ID WHERE A2.PRODUCT_REF = P.ID)
);

UPDATE PRODUCTS p
SET CLOSE_DATE = CURRENT_DATE WHERE p.
PRODUCT_TYPE_ID = (SELECT ID FROM PRODUCT_TYPE WHERE NAME = 'КРЕДИТ')
AND p.CLOSE_DATE IS NULL
AND (
  SELECT SUM(CASE WHEN r.DT = 1 THEN r.SUM ELSE 0 END)
  FROM RECORDS r JOIN ACCOUNTS a ON r.ACC_REF = a.ID
  WHERE a.PRODUCT_REF = p.ID ) = ( 
  SELECT SUM(r.SUM)
  FROM RECORDS r JOIN ACCOUNTS a ON r.ACC_REF = a.ID
  WHERE a.PRODUCT_REF = p.ID
) 
AND NOT EXISTS ( 
  SELECT 1 FROM RECORDS r
  WHERE r.ACC_REF IN ( 
    SELECT ID FROM ACCOUNTS WHERE PRODUCT_REF = p.ID
) AND r.DT = 0
);
