INSERT INTO CLIENTS (NAME, PLACE_OF_BIRTH, DATE_OF_BIRTH, ADDRESS, PASSPORT) VALUES
('Иванов Иван Иванович', 'Москва', '1980-01-01', 'ул. Ленина, д.1', '1234 567890'),
('Петров Петр Петрович', 'Санкт-Петербург', '1990-02-02', 'ул. Пушкина, д.2', '2345 678901');

INSERT INTO PRODUCT_TYPE (NAME, BEGIN_DATE, END_DATE) VALUES
('КРЕДИТ', '2023-01-01', NULL),
('ДЕПОЗИТ', '2023-01-01', NULL),
('КАРТА', '2023-01-01', NULL);

INSERT INTO PRODUCTS (PRODUCT_TYPE_ID, NAME, CLIENT_REF, OPEN_DATE) VALUES
(1, 'Кредит на покупку жилья', 1, '2023-02-01'),
(2, 'Депозит на 1 год', 2, '2023-03-01');

INSERT INTO ACCOUNTS (NAME, CLIENT_REF, OPEN_DATE, PRODUCT_REF, ACC_NUM) VALUES
('Кредит Жилье', 1, '2023-02-01', 1, '40817810412345678901'),
('Депозит 1 год', 2, '2023-03-01', 2, '40817810465432198765');

INSERT INTO TARIFS (NAME, COST) VALUES
('Тариф 1', 100),
('Тариф 2', 200);

INSERT INTO RECORDS (DT, ACC_REF, OPER_DATE, SUM) VALUES 
(1, 1, '2023-02-05', 50000), -- Дебет
(0, 2, '2023-03-05', 20000); -- Кредит
