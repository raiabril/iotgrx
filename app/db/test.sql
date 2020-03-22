--- Generator for SQL test DB
INSERT INTO "user" (id, date_created, username, email, image_file, password, token, token_expiration, admin, active) VALUES(1, '2020-03-08 18:49:58.639010', 'raiabril', 'rai@ingmechs.com', 'default.jpg', '$2b$12$4rr0Y1.mYveGJuAtBgLTFOB.nRzrZcpYALYB4dBLwASW.l2Woi4L2', 'jdOKcZ370cH/XMGJhnGPPKA9mgkSUj6I', '2020-03-08 19:50:10.827777', 0, 0);

INSERT INTO device (id, date_created, name, code, user_id) VALUES(1, '2020-03-08 00:00:00', 'Macetas', 'ESP-32', 1);
INSERT INTO device (id, date_created, name, code, user_id) VALUES(2, '2020-03-10 00:00:00', 'Weather Station', 'weatherStation', 1);
INSERT INTO device (id, date_created, name, code, user_id) VALUES(3, '2020-03-22 19:20:00', 'Fucar18', 'fucar18', 1);


INSERT INTO sensor (id, date_created, name, code, device_id) VALUES(1, '2020-03-08 00:00:00', 'R - Moisture 1 ( )', 'MOIS_1', 1);
INSERT INTO sensor (id, date_created, name, code, device_id) VALUES(2, '2020-03-08 00:00:00', 'R - Moisture 2 ( )', 'MOIS_2', 1);
INSERT INTO sensor (id, date_created, name, code, device_id) VALUES(3, '2020-03-08 00:00:00', 'R - External Temperature ( )', 'TEMP', 1);
INSERT INTO sensor (id, date_created, name, code, device_id) VALUES(4, '2020-03-08 00:00:00', 'R - Luminosity ( )', 'LIGHT', 1);
INSERT INTO sensor (id, date_created, name, code, device_id) VALUES(5, '2020-03-08 00:00:00', 'R - Current ( )', 'NONE_1', 1);
INSERT INTO sensor (id, date_created, name, code, device_id) VALUES(6, '2020-03-10 00:00:00', 'W - Temperature (C)', 'wTEMP', 2);
INSERT INTO sensor (id, date_created, name, code, device_id) VALUES(7, '2020-03-10 00:00:00', 'W - Humidity (%)', 'wHUMI', 2);
INSERT INTO sensor (id, date_created, name, code, device_id) VALUES(8, '2020-03-10 00:00:00', 'W - Est. Altitude (m)', 'wALTI', 2);
INSERT INTO sensor (id, date_created, name, code, device_id) VALUES(9, '2020-03-10 00:00:00', 'W - Pressure (hPa)', 'wPRES', 2);
INSERT INTO sensor (id, date_created, name, code, device_id) VALUES(10, '2020-03-10 00:00:00', 'W - CO2 (ppm)', 'weCO2', 2);
INSERT INTO sensor (id, date_created, name, code, device_id) VALUES(11, '2020-03-10 00:00:00', 'W - TVOC ( )', 'wTVOC', 2);
INSERT INTO sensor (id, date_created, name, code, device_id) VALUES(12, '2020-03-11 00:00:00', 'W - PM2.5 (ug/m3)', 'wPM25', 2);
INSERT INTO sensor (id, date_created, name, code, device_id) VALUES(13, '2020-03-11 00:00:00', 'W - PM10 (ug/m3)', 'wPM10', 2);
INSERT INTO sensor (id, date_created, name, code, device_id) VALUES(14, '2020-03-22 19:20:00', 'Solar Voltage (V)', 'fVOLT', 3);
INSERT INTO sensor (id, date_created, name, code, device_id) VALUES(15, '2020-03-22 19:20:00', 'Solar Current (mA)', 'fCURRENT', 3);
INSERT INTO sensor (id, date_created, name, code, device_id) VALUES(16, '2020-03-22 19:20:00', 'Solar Luminosity (%)', 'fLIGHT', 3);
INSERT INTO sensor (id, date_created, name, code, device_id) VALUES(17, '2020-03-22 19:20:00', 'Moisture 2 (%)', 'fMOIS2', 3);
INSERT INTO sensor (id, date_created, name, code, device_id) VALUES(18, '2020-03-22 19:20:00', 'Moisture 1 (%)', 'fMOIS1', 3);
INSERT INTO sensor (id, date_created, name, code, device_id) VALUES(19, '2020-03-22 19:20:00', 'PM10 (ug/m3)', 'fPM10', 3);
INSERT INTO sensor (id, date_created, name, code, device_id) VALUES(20, '2020-03-22 19:20:00', 'PM2.5 (ug/m3)', 'fPM25', 3);
INSERT INTO sensor (id, date_created, name, code, device_id) VALUES(21, '2020-03-22 19:20:00', 'Est. Altitude (m)', 'fALTI', 3);
INSERT INTO sensor (id, date_created, name, code, device_id) VALUES(22, '2020-03-22 19:20:00', 'Pressure (hPa)', 'fPRES', 3);
INSERT INTO sensor (id, date_created, name, code, device_id) VALUES(23, '2020-03-22 19:20:00', 'Humidity (%)', 'fHUMI', 3);
INSERT INTO sensor (id, date_created, name, code, device_id) VALUES(24, '2020-03-22 19:20:00', 'Temperatue (C)', 'fTEMP', 3);

INSERT INTO event (id, date_created, value, boot, user_id, sensor_code, device_code) VALUES(8467, '2020-03-22 18:19:32.142997', 0.24225, 1, '1', 'fVOLT', 'fucar18');
INSERT INTO event (id, date_created, value, boot, user_id, sensor_code, device_code) VALUES(8466, '2020-03-22 18:19:32.091966', -22.86229, 1, '1', 'fCURRENT', 'fucar18');
INSERT INTO event (id, date_created, value, boot, user_id, sensor_code, device_code) VALUES(8465, '2020-03-22 18:19:32.061569', 16.48596, 1, '1', 'fLIGHT', 'fucar18');
INSERT INTO event (id, date_created, value, boot, user_id, sensor_code, device_code) VALUES(8464, '2020-03-22 18:19:32.029831', 75.51086, 1, '1', 'fMOIS2', 'fucar18');
INSERT INTO event (id, date_created, value, boot, user_id, sensor_code, device_code) VALUES(8463, '2020-03-22 18:19:31.999854', 62.1287, 1, '1', 'fMOIS1', 'fucar18');
INSERT INTO event (id, date_created, value, boot, user_id, sensor_code, device_code) VALUES(8462, '2020-03-22 18:19:31.966463', 10.7575, 1, '1', 'fPM10', 'fucar18');
INSERT INTO event (id, date_created, value, boot, user_id, sensor_code, device_code) VALUES(8461, '2020-03-22 18:19:31.934582', 2.70125, 1, '1', 'fPM25', 'fucar18');
INSERT INTO event (id, date_created, value, boot, user_id, sensor_code, device_code) VALUES(8460, '2020-03-22 18:19:31.895417', 657.2244, 1, '1', 'fALTI', 'fucar18');
INSERT INTO event (id, date_created, value, boot, user_id, sensor_code, device_code) VALUES(8459, '2020-03-22 18:19:31.860934', 936.7608, 1, '1', 'fPRES', 'fucar18');
INSERT INTO event (id, date_created, value, boot, user_id, sensor_code, device_code) VALUES(8458, '2020-03-22 18:19:31.824874', 41.3297, 1, '1', 'fHUMI', 'fucar18');
INSERT INTO event (id, date_created, value, boot, user_id, sensor_code, device_code) VALUES(8457, '2020-03-22 18:19:31.777903', 20.7324, 1, '1', 'fTEMP', 'fucar18');
INSERT INTO event (id, date_created, value, boot, user_id, sensor_code, device_code) VALUES(8456, '2020-03-22 18:16:03.430841', 0.107115, 1, '1', 'fVOLT', 'fucar18');
INSERT INTO event (id, date_created, value, boot, user_id, sensor_code, device_code) VALUES(8455, '2020-03-22 18:16:03.393150', -21.26945, 1, '1', 'fCURRENT', 'fucar18');
INSERT INTO event (id, date_created, value, boot, user_id, sensor_code, device_code) VALUES(8454, '2020-03-22 18:16:03.363544', 21.75678, 1, '1', 'fLIGHT', 'fucar18');
INSERT INTO event (id, date_created, value, boot, user_id, sensor_code, device_code) VALUES(8453, '2020-03-22 18:16:03.333818', 84.45763, 1, '1', 'fMOIS2', 'fucar18');
INSERT INTO event (id, date_created, value, boot, user_id, sensor_code, device_code) VALUES(8452, '2020-03-22 18:16:03.303135', 84.45422, 1, '1', 'fMOIS1', 'fucar18');
INSERT INTO event (id, date_created, value, boot, user_id, sensor_code, device_code) VALUES(8451, '2020-03-22 18:16:03.254310', 5.65375, 1, '1', 'fpm10', 'fucar18');
INSERT INTO event (id, date_created, value, boot, user_id, sensor_code, device_code) VALUES(8450, '2020-03-22 18:16:03.218675', 3.082501, 1, '1', 'fpm25', 'fucar18');
INSERT INTO event (id, date_created, value, boot, user_id, sensor_code, device_code) VALUES(8449, '2020-03-22 18:16:03.192484', 656.6638, 1, '1', 'fALTI', 'fucar18');
INSERT INTO event (id, date_created, value, boot, user_id, sensor_code, device_code) VALUES(8448, '2020-03-22 18:16:03.161760', 936.8243, 1, '1', 'fPRES', 'fucar18');
INSERT INTO event (id, date_created, value, boot, user_id, sensor_code, device_code) VALUES(8447, '2020-03-22 18:16:03.126353', 43.3632, 1, '1', 'fHUMI', 'fucar18');
INSERT INTO event (id, date_created, value, boot, user_id, sensor_code, device_code) VALUES(8446, '2020-03-22 18:16:03.091733', 20.77212, 1, '1', 'fTEMP', 'fucar18');
INSERT INTO event (id, date_created, value, boot, user_id, sensor_code, device_code) VALUES(8445, '2020-03-22 18:13:36.783577', 83.52, 1, '1', 'fMOIS1', 'fucar18');
INSERT INTO event (id, date_created, value, boot, user_id, sensor_code, device_code) VALUES(8444, '2020-03-22 18:13:36.749051', 3.94, 1, '1', 'fpm10', 'fucar18');
INSERT INTO event (id, date_created, value, boot, user_id, sensor_code, device_code) VALUES(8443, '2020-03-22 18:13:36.716699', 2.35, 1, '1', 'fpm25', 'fucar18');
INSERT INTO event (id, date_created, value, boot, user_id, sensor_code, device_code) VALUES(8442, '2020-03-22 18:13:36.687624', 657.51, 1, '1', 'fALTI', 'fucar18');
INSERT INTO event (id, date_created, value, boot, user_id, sensor_code, device_code) VALUES(8441, '2020-03-22 18:13:36.653780', 936.73, 1, '1', 'fPRES', 'fucar18');
INSERT INTO event (id, date_created, value, boot, user_id, sensor_code, device_code) VALUES(8440, '2020-03-22 18:13:36.619084', 43.84, 1, '1', 'fHUMI', 'fucar18');
INSERT INTO event (id, date_created, value, boot, user_id, sensor_code, device_code) VALUES(8439, '2020-03-22 18:13:36.581813', 20.65, 1, '1', 'fTEMP', 'fucar18');
INSERT INTO event (id, date_created, value, boot, user_id, sensor_code, device_code) VALUES(8438, '2020-03-22 18:09:26.768446', 83.1, 1, '1', 'fMOIS1', 'fucar18');
INSERT INTO event (id, date_created, value, boot, user_id, sensor_code, device_code) VALUES(8437, '2020-03-22 18:09:26.739165', 5.99, 1, '1', 'fpm10', 'fucar18');
INSERT INTO event (id, date_created, value, boot, user_id, sensor_code, device_code) VALUES(8436, '2020-03-22 18:09:26.708631', 2.97, 1, '1', 'fpm25', 'fucar18');
INSERT INTO event (id, date_created, value, boot, user_id, sensor_code, device_code) VALUES(8435, '2020-03-22 18:09:26.676754', 657.88, 1, '1', 'fALTI', 'fucar18');
INSERT INTO event (id, date_created, value, boot, user_id, sensor_code, device_code) VALUES(8434, '2020-03-22 18:09:26.649017', 936.69, 1, '1', 'fPRES', 'fucar18');
INSERT INTO event (id, date_created, value, boot, user_id, sensor_code, device_code) VALUES(8433, '2020-03-22 18:09:26.621251', 45.34, 1, '1', 'fHUMI', 'fucar18');
INSERT INTO event (id, date_created, value, boot, user_id, sensor_code, device_code) VALUES(8432, '2020-03-22 18:09:26.590946', 20.33, 1, '1', 'fTEMP', 'fucar18');
INSERT INTO event (id, date_created, value, boot, user_id, sensor_code, device_code) VALUES(8431, '2020-03-22 18:02:31.941446', 0.140881, 1, '1', 'fVOLT', 'fucar18');
INSERT INTO event (id, date_created, value, boot, user_id, sensor_code, device_code) VALUES(8430, '2020-03-22 18:02:31.908952', -21.41005, 1, '1', 'fCURRENT', 'fucar18');
INSERT INTO event (id, date_created, value, boot, user_id, sensor_code, device_code) VALUES(8429, '2020-03-22 18:02:31.875318', 23.78364, 1, '1', 'fLIGHT', 'fucar18');
INSERT INTO event (id, date_created, value, boot, user_id, sensor_code, device_code) VALUES(8428, '2020-03-22 18:02:31.841905', 83.01172, 1, '1', 'fMOIS2', 'fucar18');
INSERT INTO event (id, date_created, value, boot, user_id, sensor_code, device_code) VALUES(8427, '2020-03-22 18:02:31.796754', 83.03736, 1, '1', 'fMOIS1', 'fucar18');
INSERT INTO event (id, date_created, value, boot, user_id, sensor_code, device_code) VALUES(8426, '2020-03-22 18:02:31.765655', 11.55625, 1, '1', 'fpm10', 'fucar18');
INSERT INTO event (id, date_created, value, boot, user_id, sensor_code, device_code) VALUES(8425, '2020-03-22 18:02:31.735720', 3.865001, 1, '1', 'fpm25', 'fucar18');
INSERT INTO event (id, date_created, value, boot, user_id, sensor_code, device_code) VALUES(8424, '2020-03-22 18:02:31.650006', 658.4341, 1, '1', 'fALTI', 'fucar18');
INSERT INTO event (id, date_created, value, boot, user_id, sensor_code, device_code) VALUES(8423, '2020-03-22 18:02:31.617308', 936.6242, 1, '1', 'fPRES', 'fucar18');
INSERT INTO event (id, date_created, value, boot, user_id, sensor_code, device_code) VALUES(8422, '2020-03-22 18:02:31.560967', 50.49067, 1, '1', 'fHUMI', 'fucar18');
INSERT INTO event (id, date_created, value, boot, user_id, sensor_code, device_code) VALUES(8421, '2020-03-22 18:02:31.461539', 19.06178, 1, '1', 'fTEMP', 'fucar18');
INSERT INTO event (id, date_created, value, boot, user_id, sensor_code, device_code) VALUES(8420, '2020-03-22 17:59:44.594550', 83.97314, 1, '1', 'fMOIS2', 'fucar18');
INSERT INTO event (id, date_created, value, boot, user_id, sensor_code, device_code) VALUES(8419, '2020-03-22 17:59:44.544518', 84.85641, 1, '1', 'fMOIS1', 'fucar18');
INSERT INTO event (id, date_created, value, boot, user_id, sensor_code, device_code) VALUES(8418, '2020-03-22 17:59:44.494795', 17.28874, 1, '1', 'fpm10', 'fucar18');
INSERT INTO event (id, date_created, value, boot, user_id, sensor_code, device_code) VALUES(8417, '2020-03-22 17:59:44.452223', 6.001252, 1, '1', 'fpm25', 'fucar18');
INSERT INTO event (id, date_created, value, boot, user_id, sensor_code, device_code) VALUES(8416, '2020-03-22 17:59:44.392625', 658.4461, 1, '1', 'fALTI', 'fucar18');
INSERT INTO event (id, date_created, value, boot, user_id, sensor_code, device_code) VALUES(8415, '2020-03-22 17:59:44.332018', 936.6234, 1, '1', 'fPRES', 'fucar18');
INSERT INTO event (id, date_created, value, boot, user_id, sensor_code, device_code) VALUES(8414, '2020-03-22 17:59:44.295353', 55.17512, 1, '1', 'fHUMI', 'fucar18');
INSERT INTO event (id, date_created, value, boot, user_id, sensor_code, device_code) VALUES(8413, '2020-03-22 17:59:44.252763', 17.83881, 1, '1', 'fTEMP', 'fucar18');
INSERT INTO event (id, date_created, value, boot, user_id, sensor_code, device_code) VALUES(8412, '2020-03-22 17:28:09.078121', 77.22417, 1, '1', 'fMOIS2', 'fucar18');
INSERT INTO event (id, date_created, value, boot, user_id, sensor_code, device_code) VALUES(8411, '2020-03-22 17:28:09.044810', 80.71111, 1, '1', 'fMOIS1', 'fucar18');
INSERT INTO event (id, date_created, value, boot, user_id, sensor_code, device_code) VALUES(8410, '2020-03-22 17:28:09.010379', 25.62249, 1, '1', 'fpm10', 'fucar18');
INSERT INTO event (id, date_created, value, boot, user_id, sensor_code, device_code) VALUES(8409, '2020-03-22 17:28:08.981196', 9.882498, 1, '1', 'fpm25', 'fucar18');
INSERT INTO event (id, date_created, value, boot, user_id, sensor_code, device_code) VALUES(8408, '2020-03-22 17:28:08.948224', 661.139, 1, '1', 'fALTI', 'fucar18');
INSERT INTO event (id, date_created, value, boot, user_id, sensor_code, device_code) VALUES(8407, '2020-03-22 17:28:08.905603', 936.3197, 1, '1', 'fPRES', 'fucar18');
INSERT INTO event (id, date_created, value, boot, user_id, sensor_code, device_code) VALUES(8406, '2020-03-22 17:28:08.855140', 40.7289, 1, '1', 'fHUMI', 'fucar18');
INSERT INTO event (id, date_created, value, boot, user_id, sensor_code, device_code) VALUES(8405, '2020-03-22 17:28:08.810681', 22.8439, 1, '1', 'fTEMP', 'fucar18');
INSERT INTO event (id, date_created, value, boot, user_id, sensor_code, device_code) VALUES(8404, '2020-03-22 17:25:43.537614', 84.86227, 1, '1', 'fMOIS2', 'fucar18');
INSERT INTO event (id, date_created, value, boot, user_id, sensor_code, device_code) VALUES(8403, '2020-03-22 17:25:43.501796', 84.53797, 1, '1', 'fMOIS1', 'fucar18');
INSERT INTO event (id, date_created, value, boot, user_id, sensor_code, device_code) VALUES(8402, '2020-03-22 17:25:43.470520', 32.08126, 1, '1', 'fpm10', 'fucar18');
INSERT INTO event (id, date_created, value, boot, user_id, sensor_code, device_code) VALUES(8401, '2020-03-22 17:25:43.439665', 9.911251, 1, '1', 'fpm25', 'fucar18');
INSERT INTO event (id, date_created, value, boot, user_id, sensor_code, device_code) VALUES(8400, '2020-03-22 17:25:43.406737', 660.5139, 1, '1', 'fALTI', 'fucar18');
INSERT INTO event (id, date_created, value, boot, user_id, sensor_code, device_code) VALUES(8399, '2020-03-22 17:25:43.374191', 936.3897, 1, '1', 'fPRES', 'fucar18');
INSERT INTO event (id, date_created, value, boot, user_id, sensor_code, device_code) VALUES(8398, '2020-03-22 17:25:43.337052', 43.0873, 1, '1', 'fHUMI', 'fucar18');
INSERT INTO event (id, date_created, value, boot, user_id, sensor_code, device_code) VALUES(8397, '2020-03-22 17:25:43.298270', 23.0037, 1, '1', 'fTEMP', 'fucar18');
INSERT INTO event (id, date_created, value, boot, user_id, sensor_code, device_code) VALUES(8396, '2020-03-22 13:39:44.959712', 0, 1, '1', 'NONE_5', 'ESP-32');
INSERT INTO event (id, date_created, value, boot, user_id, sensor_code, device_code) VALUES(8395, '2020-03-22 13:39:44.926833', 0, 1, '1', 'NONE_4', 'ESP-32');
INSERT INTO event (id, date_created, value, boot, user_id, sensor_code, device_code) VALUES(8394, '2020-03-22 13:39:44.886822', 0, 1, '1', 'NONE_3', 'ESP-32');
INSERT INTO event (id, date_created, value, boot, user_id, sensor_code, device_code) VALUES(8393, '2020-03-22 13:39:44.855480', 436, 1, '1', 'NONE_2', 'ESP-32');
INSERT INTO event (id, date_created, value, boot, user_id, sensor_code, device_code) VALUES(8392, '2020-03-22 13:39:44.819553', 1219, 1, '1', 'LIGHT', 'ESP-32');
INSERT INTO event (id, date_created, value, boot, user_id, sensor_code, device_code) VALUES(8391, '2020-03-22 13:39:44.779029', 181, 1, '1', 'TEMP', 'ESP-32');
INSERT INTO event (id, date_created, value, boot, user_id, sensor_code, device_code) VALUES(8390, '2020-03-22 13:39:44.740365', 1873, 1, '1', 'NONE_1', 'ESP-32');
INSERT INTO event (id, date_created, value, boot, user_id, sensor_code, device_code) VALUES(8389, '2020-03-22 13:39:44.709694', 713, 1, '1', 'MOIS_2', 'ESP-32');
INSERT INTO event (id, date_created, value, boot, user_id, sensor_code, device_code) VALUES(8388, '2020-03-22 13:39:44.675936', 820, 1, '1', 'MOIS_1', 'ESP-32');
INSERT INTO event (id, date_created, value, boot, user_id, sensor_code, device_code) VALUES(8387, '2020-03-22 13:26:53.263107', 0, 1, '1', 'NONE_5', 'ESP-32');
INSERT INTO event (id, date_created, value, boot, user_id, sensor_code, device_code) VALUES(8386, '2020-03-22 13:26:53.232626', 0, 1, '1', 'NONE_4', 'ESP-32');
INSERT INTO event (id, date_created, value, boot, user_id, sensor_code, device_code) VALUES(8385, '2020-03-22 13:26:53.197701', 0, 1, '1', 'NONE_3', 'ESP-32');
INSERT INTO event (id, date_created, value, boot, user_id, sensor_code, device_code) VALUES(8384, '2020-03-22 13:26:53.157228', 485, 1, '1', 'NONE_2', 'ESP-32');
INSERT INTO event (id, date_created, value, boot, user_id, sensor_code, device_code) VALUES(8383, '2020-03-22 13:26:53.120370', 0, 1, '1', 'LIGHT', 'ESP-32');
INSERT INTO event (id, date_created, value, boot, user_id, sensor_code, device_code) VALUES(8382, '2020-03-22 13:26:53.083614', 502, 1, '1', 'TEMP', 'ESP-32');
INSERT INTO event (id, date_created, value, boot, user_id, sensor_code, device_code) VALUES(8381, '2020-03-22 13:26:53.054425', 132, 1, '1', 'NONE_1', 'ESP-32');
INSERT INTO event (id, date_created, value, boot, user_id, sensor_code, device_code) VALUES(8380, '2020-03-22 13:26:53.021857', 368, 1, '1', 'MOIS_2', 'ESP-32');
INSERT INTO event (id, date_created, value, boot, user_id, sensor_code, device_code) VALUES(8379, '2020-03-22 13:26:52.987632', 400, 1, '1', 'MOIS_1', 'ESP-32');
INSERT INTO event (id, date_created, value, boot, user_id, sensor_code, device_code) VALUES(8378, '2020-03-22 13:22:13.595295', 0, 1, '1', 'NONE_5', 'ESP-32');
INSERT INTO event (id, date_created, value, boot, user_id, sensor_code, device_code) VALUES(8377, '2020-03-22 13:22:13.564162', 0, 1, '1', 'NONE_4', 'ESP-32');
INSERT INTO event (id, date_created, value, boot, user_id, sensor_code, device_code) VALUES(8376, '2020-03-22 13:22:13.527905', 0, 1, '1', 'NONE_3', 'ESP-32');
INSERT INTO event (id, date_created, value, boot, user_id, sensor_code, device_code) VALUES(8375, '2020-03-22 13:22:13.488603', 474, 1, '1', 'NONE_2', 'ESP-32');
INSERT INTO event (id, date_created, value, boot, user_id, sensor_code, device_code) VALUES(8374, '2020-03-22 13:22:13.456377', 0, 1, '1', 'LIGHT', 'ESP-32');
INSERT INTO event (id, date_created, value, boot, user_id, sensor_code, device_code) VALUES(8373, '2020-03-22 13:22:13.429260', 84, 1, '1', 'TEMP', 'ESP-32');
INSERT INTO event (id, date_created, value, boot, user_id, sensor_code, device_code) VALUES(8372, '2020-03-22 13:22:13.397358', 128, 1, '1', 'NONE_1', 'ESP-32');
INSERT INTO event (id, date_created, value, boot, user_id, sensor_code, device_code) VALUES(8371, '2020-03-22 13:22:13.364000', 105, 1, '1', 'MOIS_2', 'ESP-32');
INSERT INTO event (id, date_created, value, boot, user_id, sensor_code, device_code) VALUES(8370, '2020-03-22 13:22:13.329883', 32, 1, '1', 'MOIS_1', 'ESP-32');
INSERT INTO event (id, date_created, value, boot, user_id, sensor_code, device_code) VALUES(8369, '2020-03-22 13:21:20.180706', 0, 1, '1', 'NONE_5', 'ESP-32');
INSERT INTO event (id, date_created, value, boot, user_id, sensor_code, device_code) VALUES(8368, '2020-03-22 13:21:20.149593', 0, 1, '1', 'NONE_4', 'ESP-32');
INSERT INTO event (id, date_created, value, boot, user_id, sensor_code, device_code) VALUES(8367, '2020-03-22 13:21:20.104330', 0, 1, '1', 'NONE_3', 'ESP-32');
INSERT INTO event (id, date_created, value, boot, user_id, sensor_code, device_code) VALUES(8366, '2020-03-22 13:21:20.067576', 496, 1, '1', 'NONE_2', 'ESP-32');
INSERT INTO event (id, date_created, value, boot, user_id, sensor_code, device_code) VALUES(8365, '2020-03-22 13:21:20.035847', 0, 1, '1', 'LIGHT', 'ESP-32');
INSERT INTO event (id, date_created, value, boot, user_id, sensor_code, device_code) VALUES(8364, '2020-03-22 13:21:20.003090', 386, 1, '1', 'TEMP', 'ESP-32');
INSERT INTO event (id, date_created, value, boot, user_id, sensor_code, device_code) VALUES(8363, '2020-03-22 13:21:19.961776', 134, 1, '1', 'NONE_1', 'ESP-32');
INSERT INTO event (id, date_created, value, boot, user_id, sensor_code, device_code) VALUES(8362, '2020-03-22 13:21:19.931562', 320, 1, '1', 'MOIS_2', 'ESP-32');
INSERT INTO event (id, date_created, value, boot, user_id, sensor_code, device_code) VALUES(8361, '2020-03-22 13:21:19.885647', 296, 1, '1', 'MOIS_1', 'ESP-32');
INSERT INTO event (id, date_created, value, boot, user_id, sensor_code, device_code) VALUES(8360, '2020-03-22 10:59:41.465299', 0, 43, '1', 'NONE_5', 'ESP-32');
INSERT INTO event (id, date_created, value, boot, user_id, sensor_code, device_code) VALUES(8359, '2020-03-22 10:59:41.427809', 0, 43, '1', 'NONE_4', 'ESP-32');
INSERT INTO event (id, date_created, value, boot, user_id, sensor_code, device_code) VALUES(8358, '2020-03-22 10:59:41.393646', 0, 43, '1', 'NONE_3', 'ESP-32');
INSERT INTO event (id, date_created, value, boot, user_id, sensor_code, device_code) VALUES(8357, '2020-03-22 10:59:41.357183', 544, 43, '1', 'NONE_2', 'ESP-32');
INSERT INTO event (id, date_created, value, boot, user_id, sensor_code, device_code) VALUES(8356, '2020-03-22 10:59:41.317311', 3327, 43, '1', 'LIGHT', 'ESP-32');
INSERT INTO event (id, date_created, value, boot, user_id, sensor_code, device_code) VALUES(8355, '2020-03-22 10:59:41.082501', 1437, 43, '1', 'TEMP', 'ESP-32');
INSERT INTO event (id, date_created, value, boot, user_id, sensor_code, device_code) VALUES(8354, '2020-03-22 10:59:40.732832', 1859, 43, '1', 'NONE_1', 'ESP-32');
INSERT INTO event (id, date_created, value, boot, user_id, sensor_code, device_code) VALUES(8353, '2020-03-22 10:59:40.610384', 884, 43, '1', 'MOIS_2', 'ESP-32');
INSERT INTO event (id, date_created, value, boot, user_id, sensor_code, device_code) VALUES(8352, '2020-03-22 10:59:40.220399', 1435, 43, '1', 'MOIS_1', 'ESP-32');
INSERT INTO event (id, date_created, value, boot, user_id, sensor_code, device_code) VALUES(8351, '2020-03-22 10:29:31.901579', 0, 42, '1', 'NONE_5', 'ESP-32');
INSERT INTO event (id, date_created, value, boot, user_id, sensor_code, device_code) VALUES(8350, '2020-03-22 10:29:31.855174', 0, 42, '1', 'NONE_4', 'ESP-32');
INSERT INTO event (id, date_created, value, boot, user_id, sensor_code, device_code) VALUES(8349, '2020-03-22 10:29:31.819154', 0, 42, '1', 'NONE_3', 'ESP-32');
INSERT INTO event (id, date_created, value, boot, user_id, sensor_code, device_code) VALUES(8348, '2020-03-22 10:29:31.773439', 576, 42, '1', 'NONE_2', 'ESP-32');
INSERT INTO event (id, date_created, value, boot, user_id, sensor_code, device_code) VALUES(8347, '2020-03-22 10:29:31.734676', 3311, 42, '1', 'LIGHT', 'ESP-32');
INSERT INTO event (id, date_created, value, boot, user_id, sensor_code, device_code) VALUES(8346, '2020-03-22 10:29:31.694628', 1410, 42, '1', 'TEMP', 'ESP-32');
INSERT INTO event (id, date_created, value, boot, user_id, sensor_code, device_code) VALUES(8345, '2020-03-22 10:29:31.656674', 1860, 42, '1', 'NONE_1', 'ESP-32');
INSERT INTO event (id, date_created, value, boot, user_id, sensor_code, device_code) VALUES(8344, '2020-03-22 10:29:31.597269', 880, 42, '1', 'MOIS_2', 'ESP-32');
INSERT INTO event (id, date_created, value, boot, user_id, sensor_code, device_code) VALUES(8343, '2020-03-22 10:29:31.553688', 1439, 42, '1', 'MOIS_1', 'ESP-32');
INSERT INTO event (id, date_created, value, boot, user_id, sensor_code, device_code) VALUES(8342, '2020-03-22 09:59:24.107738', 0, 41, '1', 'NONE_5', 'ESP-32');
INSERT INTO event (id, date_created, value, boot, user_id, sensor_code, device_code) VALUES(8341, '2020-03-22 09:59:24.056206', 0, 41, '1', 'NONE_4', 'ESP-32');
INSERT INTO event (id, date_created, value, boot, user_id, sensor_code, device_code) VALUES(8340, '2020-03-22 09:59:24.022998', 0, 41, '1', 'NONE_3', 'ESP-32');
INSERT INTO event (id, date_created, value, boot, user_id, sensor_code, device_code) VALUES(8339, '2020-03-22 09:59:23.984219', 584, 41, '1', 'NONE_2', 'ESP-32');
INSERT INTO event (id, date_created, value, boot, user_id, sensor_code, device_code) VALUES(8338, '2020-03-22 09:59:23.946514', 3335, 41, '1', 'LIGHT', 'ESP-32');
INSERT INTO event (id, date_created, value, boot, user_id, sensor_code, device_code) VALUES(8337, '2020-03-22 09:59:23.909955', 1411, 41, '1', 'TEMP', 'ESP-32');
INSERT INTO event (id, date_created, value, boot, user_id, sensor_code, device_code) VALUES(8336, '2020-03-22 09:59:23.872918', 1861, 41, '1', 'NONE_1', 'ESP-32');
INSERT INTO event (id, date_created, value, boot, user_id, sensor_code, device_code) VALUES(8335, '2020-03-22 09:59:23.843702', 892, 41, '1', 'MOIS_2', 'ESP-32');
INSERT INTO event (id, date_created, value, boot, user_id, sensor_code, device_code) VALUES(8334, '2020-03-22 09:59:23.795826', 1430, 41, '1', 'MOIS_1', 'ESP-32');
INSERT INTO event (id, date_created, value, boot, user_id, sensor_code, device_code) VALUES(8333, '2020-03-22 09:29:15.802045', 0, 40, '1', 'NONE_5', 'ESP-32');
INSERT INTO event (id, date_created, value, boot, user_id, sensor_code, device_code) VALUES(8332, '2020-03-22 09:29:15.764881', 0, 40, '1', 'NONE_4', 'ESP-32');
INSERT INTO event (id, date_created, value, boot, user_id, sensor_code, device_code) VALUES(8331, '2020-03-22 09:29:15.722956', 0, 40, '1', 'NONE_3', 'ESP-32');
INSERT INTO event (id, date_created, value, boot, user_id, sensor_code, device_code) VALUES(8330, '2020-03-22 09:29:15.676949', 590, 40, '1', 'NONE_2', 'ESP-32');
INSERT INTO event (id, date_created, value, boot, user_id, sensor_code, device_code) VALUES(8329, '2020-03-22 09:29:15.639017', 2558, 40, '1', 'LIGHT', 'ESP-32');
INSERT INTO event (id, date_created, value, boot, user_id, sensor_code, device_code) VALUES(8328, '2020-03-22 09:29:15.601729', 1328, 40, '1', 'TEMP', 'ESP-32');
INSERT INTO event (id, date_created, value, boot, user_id, sensor_code, device_code) VALUES(8327, '2020-03-22 09:29:15.567949', 1872, 40, '1', 'NONE_1', 'ESP-32');
INSERT INTO event (id, date_created, value, boot, user_id, sensor_code, device_code) VALUES(8326, '2020-03-22 09:29:15.531567', 925, 40, '1', 'MOIS_2', 'ESP-32');
INSERT INTO event (id, date_created, value, boot, user_id, sensor_code, device_code) VALUES(8325, '2020-03-22 09:29:15.496651', 1393, 40, '1', 'MOIS_1', 'ESP-32');
INSERT INTO event (id, date_created, value, boot, user_id, sensor_code, device_code) VALUES(8324, '2020-03-22 08:59:02.961917', 0, 39, '1', 'NONE_5', 'ESP-32');
INSERT INTO event (id, date_created, value, boot, user_id, sensor_code, device_code) VALUES(8323, '2020-03-22 08:59:02.929308', 0, 39, '1', 'NONE_4', 'ESP-32');
INSERT INTO event (id, date_created, value, boot, user_id, sensor_code, device_code) VALUES(8322, '2020-03-22 08:59:02.895730', 0, 39, '1', 'NONE_3', 'ESP-32');
INSERT INTO event (id, date_created, value, boot, user_id, sensor_code, device_code) VALUES(8321, '2020-03-22 08:59:02.852934', 624, 39, '1', 'NONE_2', 'ESP-32');
INSERT INTO event (id, date_created, value, boot, user_id, sensor_code, device_code) VALUES(8320, '2020-03-22 08:59:02.821058', 2260, 39, '1', 'LIGHT', 'ESP-32');
INSERT INTO event (id, date_created, value, boot, user_id, sensor_code, device_code) VALUES(8319, '2020-03-22 08:59:02.785606', 1296, 39, '1', 'TEMP', 'ESP-32');
INSERT INTO event (id, date_created, value, boot, user_id, sensor_code, device_code) VALUES(8318, '2020-03-22 08:59:02.748449', 1919, 39, '1', 'NONE_1', 'ESP-32');
INSERT INTO event (id, date_created, value, boot, user_id, sensor_code, device_code) VALUES(8317, '2020-03-22 08:59:02.715076', 851, 39, '1', 'MOIS_2', 'ESP-32');
INSERT INTO event (id, date_created, value, boot, user_id, sensor_code, device_code) VALUES(8316, '2020-03-22 08:59:02.671410', 1424, 39, '1', 'MOIS_1', 'ESP-32');
INSERT INTO event (id, date_created, value, boot, user_id, sensor_code, device_code) VALUES(8315, '2020-03-22 08:28:44.176935', 0, 38, '1', 'NONE_5', 'ESP-32');
INSERT INTO event (id, date_created, value, boot, user_id, sensor_code, device_code) VALUES(8314, '2020-03-22 08:28:44.138336', 0, 38, '1', 'NONE_4', 'ESP-32');
INSERT INTO event (id, date_created, value, boot, user_id, sensor_code, device_code) VALUES(8313, '2020-03-22 08:28:44.088962', 0, 38, '1', 'NONE_3', 'ESP-32');
INSERT INTO event (id, date_created, value, boot, user_id, sensor_code, device_code) VALUES(8312, '2020-03-22 08:28:44.041133', 624, 38, '1', 'NONE_2', 'ESP-32');
INSERT INTO event (id, date_created, value, boot, user_id, sensor_code, device_code) VALUES(8311, '2020-03-22 08:28:43.969067', 2098, 38, '1', 'LIGHT', 'ESP-32');
INSERT INTO event (id, date_created, value, boot, user_id, sensor_code, device_code) VALUES(8310, '2020-03-22 08:28:43.916487', 1295, 38, '1', 'TEMP', 'ESP-32');
INSERT INTO event (id, date_created, value, boot, user_id, sensor_code, device_code) VALUES(8309, '2020-03-22 08:28:43.877268', 1814, 38, '1', 'NONE_1', 'ESP-32');
INSERT INTO event (id, date_created, value, boot, user_id, sensor_code, device_code) VALUES(8308, '2020-03-22 08:28:43.844029', 889, 38, '1', 'MOIS_2', 'ESP-32');
INSERT INTO event (id, date_created, value, boot, user_id, sensor_code, device_code) VALUES(8307, '2020-03-22 08:28:43.798813', 1421, 38, '1', 'MOIS_1', 'ESP-32');
INSERT INTO event (id, date_created, value, boot, user_id, sensor_code, device_code) VALUES(8306, '2020-03-22 07:58:34.935304', 0, 37, '1', 'NONE_5', 'ESP-32');
INSERT INTO event (id, date_created, value, boot, user_id, sensor_code, device_code) VALUES(8305, '2020-03-22 07:58:34.898274', 0, 37, '1', 'NONE_4', 'ESP-32');
INSERT INTO event (id, date_created, value, boot, user_id, sensor_code, device_code) VALUES(8304, '2020-03-22 07:58:34.864888', 0, 37, '1', 'NONE_3', 'ESP-32');
INSERT INTO event (id, date_created, value, boot, user_id, sensor_code, device_code) VALUES(8303, '2020-03-22 07:58:34.827486', 626, 37, '1', 'NONE_2', 'ESP-32');
INSERT INTO event (id, date_created, value, boot, user_id, sensor_code, device_code) VALUES(8302, '2020-03-22 07:58:34.795961', 2057, 37, '1', 'LIGHT', 'ESP-32');
INSERT INTO event (id, date_created, value, boot, user_id, sensor_code, device_code) VALUES(8301, '2020-03-22 07:58:34.762457', 1264, 37, '1', 'TEMP', 'ESP-32');
INSERT INTO event (id, date_created, value, boot, user_id, sensor_code, device_code) VALUES(8300, '2020-03-22 07:58:34.736033', 1869, 37, '1', 'NONE_1', 'ESP-32');
INSERT INTO event (id, date_created, value, boot, user_id, sensor_code, device_code) VALUES(8299, '2020-03-22 07:58:34.705881', 841, 37, '1', 'MOIS_2', 'ESP-32');
INSERT INTO event (id, date_created, value, boot, user_id, sensor_code, device_code) VALUES(8298, '2020-03-22 07:58:34.661695', 1424, 37, '1', 'MOIS_1', 'ESP-32');
INSERT INTO event (id, date_created, value, boot, user_id, sensor_code, device_code) VALUES(8297, '2020-03-22 07:28:27.666005', 0, 36, '1', 'NONE_5', 'ESP-32');
INSERT INTO event (id, date_created, value, boot, user_id, sensor_code, device_code) VALUES(8296, '2020-03-22 07:28:27.631158', 0, 36, '1', 'NONE_4', 'ESP-32');
INSERT INTO event (id, date_created, value, boot, user_id, sensor_code, device_code) VALUES(8295, '2020-03-22 07:28:27.599987', 0, 36, '1', 'NONE_3', 'ESP-32');
INSERT INTO event (id, date_created, value, boot, user_id, sensor_code, device_code) VALUES(8294, '2020-03-22 07:28:27.566245', 610, 36, '1', 'NONE_2', 'ESP-32');
INSERT INTO event (id, date_created, value, boot, user_id, sensor_code, device_code) VALUES(8293, '2020-03-22 07:28:27.535734', 1935, 36, '1', 'LIGHT', 'ESP-32');
INSERT INTO event (id, date_created, value, boot, user_id, sensor_code, device_code) VALUES(8292, '2020-03-22 07:28:27.504905', 1233, 36, '1', 'TEMP', 'ESP-32');
INSERT INTO event (id, date_created, value, boot, user_id, sensor_code, device_code) VALUES(8291, '2020-03-22 07:28:27.472090', 1863, 36, '1', 'NONE_1', 'ESP-32');
INSERT INTO event (id, date_created, value, boot, user_id, sensor_code, device_code) VALUES(8290, '2020-03-22 07:28:27.440744', 842, 36, '1', 'MOIS_2', 'ESP-32');
INSERT INTO event (id, date_created, value, boot, user_id, sensor_code, device_code) VALUES(8289, '2020-03-22 07:28:27.397161', 1410, 36, '1', 'MOIS_1', 'ESP-32');
INSERT INTO event (id, date_created, value, boot, user_id, sensor_code, device_code) VALUES(8288, '2020-03-22 06:58:21.662464', 0, 35, '1', 'NONE_5', 'ESP-32');
INSERT INTO event (id, date_created, value, boot, user_id, sensor_code, device_code) VALUES(8287, '2020-03-22 06:58:21.631118', 0, 35, '1', 'NONE_4', 'ESP-32');
INSERT INTO event (id, date_created, value, boot, user_id, sensor_code, device_code) VALUES(8286, '2020-03-22 06:58:21.596442', 0, 35, '1', 'NONE_3', 'ESP-32');
INSERT INTO event (id, date_created, value, boot, user_id, sensor_code, device_code) VALUES(8285, '2020-03-22 06:58:21.552435', 625, 35, '1', 'NONE_2', 'ESP-32');
INSERT INTO event (id, date_created, value, boot, user_id, sensor_code, device_code) VALUES(8284, '2020-03-22 06:58:21.521283', 1330, 35, '1', 'LIGHT', 'ESP-32');
INSERT INTO event (id, date_created, value, boot, user_id, sensor_code, device_code) VALUES(8283, '2020-03-22 06:58:21.475874', 1235, 35, '1', 'TEMP', 'ESP-32');
INSERT INTO event (id, date_created, value, boot, user_id, sensor_code, device_code) VALUES(8282, '2020-03-22 06:58:21.436623', 1862, 35, '1', 'NONE_1', 'ESP-32');
INSERT INTO event (id, date_created, value, boot, user_id, sensor_code, device_code) VALUES(8281, '2020-03-22 06:58:21.401382', 848, 35, '1', 'MOIS_2', 'ESP-32');
INSERT INTO event (id, date_created, value, boot, user_id, sensor_code, device_code) VALUES(8280, '2020-03-22 06:58:21.358698', 1420, 35, '1', 'MOIS_1', 'ESP-32');
INSERT INTO event (id, date_created, value, boot, user_id, sensor_code, device_code) VALUES(8279, '2020-03-22 06:28:14.374824', 0, 34, '1', 'NONE_5', 'ESP-32');
INSERT INTO event (id, date_created, value, boot, user_id, sensor_code, device_code) VALUES(8278, '2020-03-22 06:28:14.339400', 0, 34, '1', 'NONE_4', 'ESP-32');
INSERT INTO event (id, date_created, value, boot, user_id, sensor_code, device_code) VALUES(8277, '2020-03-22 06:28:14.306288', 0, 34, '1', 'NONE_3', 'ESP-32');
INSERT INTO event (id, date_created, value, boot, user_id, sensor_code, device_code) VALUES(8276, '2020-03-22 06:28:14.273639', 616, 34, '1', 'NONE_2', 'ESP-32');
INSERT INTO event (id, date_created, value, boot, user_id, sensor_code, device_code) VALUES(8275, '2020-03-22 06:28:14.234021', 674, 34, '1', 'LIGHT', 'ESP-32');
INSERT INTO event (id, date_created, value, boot, user_id, sensor_code, device_code) VALUES(8274, '2020-03-22 06:28:14.204799', 1262, 34, '1', 'TEMP', 'ESP-32');
INSERT INTO event (id, date_created, value, boot, user_id, sensor_code, device_code) VALUES(8273, '2020-03-22 06:28:14.175042', 1845, 34, '1', 'NONE_1', 'ESP-32');
INSERT INTO event (id, date_created, value, boot, user_id, sensor_code, device_code) VALUES(8272, '2020-03-22 06:28:14.145081', 857, 34, '1', 'MOIS_2', 'ESP-32');
INSERT INTO event (id, date_created, value, boot, user_id, sensor_code, device_code) VALUES(8271, '2020-03-22 06:28:14.103036', 1472, 34, '1', 'MOIS_1', 'ESP-32');
INSERT INTO event (id, date_created, value, boot, user_id, sensor_code, device_code) VALUES(8270, '2020-03-22 05:58:06.805723', 0, 33, '1', 'NONE_5', 'ESP-32');
INSERT INTO event (id, date_created, value, boot, user_id, sensor_code, device_code) VALUES(8269, '2020-03-22 05:58:06.770708', 0, 33, '1', 'NONE_4', 'ESP-32');
INSERT INTO event (id, date_created, value, boot, user_id, sensor_code, device_code) VALUES(8268, '2020-03-22 05:58:06.728282', 0, 33, '1', 'NONE_3', 'ESP-32');
