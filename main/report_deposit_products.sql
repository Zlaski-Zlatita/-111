SELECT A.*
FROM ACCOUNTS A
  JOIN PRODUCTS P ON A.PRODUCT_REF = P.ID
WHERE P.PRODUCT_TYPE_ID = (SELECT ID FROM PRODUCT_TYPE WHERE NAME = 'ДЕПОЗИТ') AND P.CLIENT_REF NOT IN (
  SELECT CLIENT_REF FROM PRODUCTS
  WHERE PRODUCT_TYPE_ID = (SELECT ID FROM PRODUCT_TYPE WHERE NAME = 'КРЕДИТ')
);


