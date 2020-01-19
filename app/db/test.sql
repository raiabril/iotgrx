--- Generator for SQL test DB
INSERT INTO "user" (id, date_created, username, email, image_file, password, token, token_expiration, admin) VALUES(1, '2019-12-29 19:42:46.104577', 'raiabril', 'rai@ingmechs.com', '5f1a00dc08529851.jpeg', '$2b$12$7eNmbcg6veM.HCQk//qVWOLl0eQN9mVCj9DlCFOVgipxK4fQBbluu', 'DWcjgju6zBKKZP4fZkKQuwXOLrG6Y3AQ', '2019-12-30 01:06:31.871776', 0);
INSERT INTO device (id, date_created, name, user_id) VALUES(1, '2019-12-12 00:00:00', 'ESP-32', 1);
INSERT INTO sensor (id, date_created, name, user_id, device_id) VALUES(1, '2019-12-12 00:00:00', 'LIGHT', 1, 1);
INSERT INTO sensor (id, date_created, name, user_id, device_id) VALUES(2, '2019-12-12 00:00:00', 'TEMP', 1, 1);
INSERT INTO sensor (id, date_created, name, user_id, device_id) VALUES(3, '2019-12-12 00:00:00', 'MOIS_1', 1, 1);
INSERT INTO sensor (id, date_created, name, user_id, device_id) VALUES(4, '2019-12-12 00:00:00', 'MOIS_2', 1, 1);
INSERT INTO sensor (id, date_created, name, user_id, device_id) VALUES(5, '2019-12-12 00:00:00', 'MOIS_3', 1, 1);
INSERT INTO sensor (id, date_created, name, user_id, device_id) VALUES(6, '2019-12-12 00:00:00', 'MOIS_4', 1, 1);
INSERT INTO sensor (id, date_created, name, user_id, device_id) VALUES(7, '2019-12-12 00:00:00', 'MOIS_5', 1, 1);
INSERT INTO sensor (id, date_created, name, user_id, device_id) VALUES(8, '2019-12-12 00:00:00', 'EMPTY_1', 1, 1);
INSERT INTO sensor (id, date_created, name, user_id, device_id) VALUES(9, '2019-12-12 00:00:00', 'EMPTY_2', 1, 1);
