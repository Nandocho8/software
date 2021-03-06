import string
import random
from django.core.mail import send_mail


def password(x):
    lower = list(string.ascii_lowercase)
    upper = list(string.ascii_uppercase)
    number = list(string.digits)
    symbol = list('@#$')

    init = list(lower + upper)
    word = list(lower + upper + number + symbol)

    temp = random.sample(init, 1) + random.sample(word, x-1)

    password = "".join(temp)

    return password


def mail(password, mail):
    subject = 'Registro Importadora Larraín'
    message = 'Estimado '+mail + \
        ' su registro en Importadora Larraín ha sido exitoso \n su contraseña para acceder es ' + password
    to_mail = str(mail)
    send_mail(subject, message, '', [to_mail],)


def comuna():
    comuna = [
        (1, 'Arica'),
        (2, 'Camarones'),
        (3, 'General Lagos'),
        (4, 'Putre'),
        (5, 'Alto Hospicio'),
        (6, 'Iquique'),
        (7, 'Camiña'),
        (8, 'Colchane'),
        (9, 'Huara'),
        (10, 'Pica'),
        (11, 'Pozo Almonte'),
        (12, 'Antofagasta'),
        (13, 'Mejillones'),
        (14, 'Sierra Gorda'),
        (15, 'Taltal'),
        (16, 'Calama'),
        (17, 'Ollague'),
        (18, 'San Pedro de Atacama'),
        (19, 'María Elena'),
        (20, 'Tocopilla'),
        (21, 'Chañaral'),
        (22, 'Diego de Almagro'),
        (23, 'Caldera'),
        (24, 'Copiapó'),
        (25, 'Tierra Amarilla'),
        (26, 'Alto del Carmen'),
        (27, 'Freirina'),
        (28, 'Huasco'),
        (29, 'Vallenar'),
        (30, 'Canela'),
        (31, 'Illapel'),
        (32, 'Los Vilos'),
        (33, 'Salamanca'),
        (34, 'Andacollo'),
        (35, 'Coquimbo'),
        (36, 'La Higuera'),
        (37, 'La Serena'),
        (38, 'Paihuaco'),
        (39, 'Vicuña'),
        (40, 'Combarbalá'),
        (41, 'Monte Patria'),
        (42, 'Ovalle'),
        (43, 'Punitaqui'),
        (44, 'Río Hurtado'),
        (45, 'Isla de Pascua'),
        (46, 'Calle Larga'),
        (47, 'Los Andes'),
        (48, 'Rinconada'),
        (49, 'San Esteban'),
        (50, 'La Ligua'),
        (51, 'Papudo'),
        (52, 'Petorca'),
        (53, 'Zapallar'),
        (54, 'Hijuelas'),
        (55, 'La Calera'),
        (56, 'La Cruz'),
        (57, 'Limache'),
        (58, 'Nogales'),
        (59, 'Olmué'),
        (60, 'Quillota'),
        (61, 'Algarrobo'),
        (62, 'Cartagena'),
        (63, 'El Quisco'),
        (64, 'El Tabo'),
        (65, 'San Antonio'),
        (66, 'Santo Domingo'),
        (67, 'Catemu'),
        (68, 'Llaillay'),
        (69, 'Panquehue'),
        (70, 'Putaendo'),
        (71, 'San Felipe'),
        (72, 'Santa María'),
        (73, 'Casablanca'),
        (74, 'Concón'),
        (75, 'Juan Fernández'),
        (76, 'Puchuncaví'),
        (77, 'Quilpué'),
        (78, 'Quintero'),
        (79, 'Valparaíso'),
        (80, 'Villa Alemana'),
        (81, 'Viña del Mar'),
        (82, 'Colina'),
        (83, 'Lampa'),
        (84, 'Tiltil'),
        (85, 'Pirque'),
        (86, 'Puente Alto'),
        (87, 'San José de Maipo'),
        (88, 'Buin'),
        (89, 'Calera de Tango'),
        (90, 'Paine'),
        (91, 'San Bernardo'),
        (92, 'Alhué'),
        (93, 'Curacaví'),
        (94, 'María Pinto'),
        (95, 'Melipilla'),
        (96, 'San Pedro'),
        (97, 'Cerrillos'),
        (98, 'Cerro Navia'),
        (99, 'Conchalí'),
        (100, 'El Bosque'),
        (101, 'Estación Central'),
        (102, 'Huechuraba'),
        (103, 'Independencia'),
        (104, 'La Cisterna'),
        (105, 'La Granja'),
        (106, 'La Florida'),
        (107, 'La Pintana'),
        (108, 'La Reina'),
        (109, 'Las Condes'),
        (110, 'Lo Barnechea'),
        (111, 'Lo Espejo'),
        (112, 'Lo Prado'),
        (113, 'Macul'),
        (114, 'Maipú'),
        (115, 'Ñuñoa'),
        (116, 'Pedro Aguirre Cerda'),
        (117, 'Peñalolén'),
        (118, 'Providencia'),
        (119, 'Pudahuel'),
        (120, 'Quilicura'),
        (121, 'Quinta Normal'),
        (122, 'Recoleta'),
        (123, 'Renca'),
        (124, 'San Miguel'),
        (125, 'San Joaquín'),
        (126, 'San Ramón'),
        (127, 'Santiago'),
        (128, 'Vitacura'),
        (129, 'El Monte'),
        (130, 'Isla de Maipo'),
        (131, 'Padre Hurtado'),
        (132, 'Peñaflor'),
        (133, 'Talagante'),
        (134, 'Codegua'),
        (135, 'Coínco'),
        (136, 'Coltauco'),
        (137, 'Doñihue'),
        (138, 'Graneros'),
        (139, 'Las Cabras'),
        (140, 'Machalí'),
        (141, 'Malloa'),
        (142, 'Mostazal'),
        (143, 'Olivar'),
        (144, 'Peumo'),
        (145, 'Pichidegua'),
        (146, 'Quinta de Tilcoco'),
        (147, 'Rancagua'),
        (148, 'Rengo'),
        (149, 'Requínoa'),
        (150, 'San Vicente de Tagua Tagua'),
        (151, 'La Estrella'),
        (152, 'Litueche'),
        (153, 'Marchihue'),
        (154, 'Navidad'),
        (155, 'Paredones'),
        (156, 'Pichilemu'),
        (157, 'Chépica'),
        (158, 'Chimbarongo'),
        (159, 'Lolol'),
        (160, 'Nancagua'),
        (161, 'Palmilla'),
        (162, 'Peralillo'),
        (163, 'Placilla'),
        (164, 'Pumanque'),
        (165, 'San Fernando'),
        (166, 'Santa Cruz'),
        (167, 'Cauquenes'),
        (168, 'Chanco'),
        (169, 'Pelluhue'),
        (170, 'Curicó'),
        (171, 'Hualañé'),
        (172, 'Licantén'),
        (173, 'Molina'),
        (174, 'Rauco'),
        (175, 'Romeral'),
        (176, 'Sagrada Familia'),
        (177, 'Teno'),
        (178, 'Vichuquén'),
        (179, 'Colbún'),
        (180, 'Linares'),
        (181, 'Longaví'),
        (182, 'Parral'),
        (183, 'Retiro'),
        (184, 'San Javier'),
        (185, 'Villa Alegre'),
        (186, 'Yerbas Buenas'),
        (187, 'Constitución'),
        (188, 'Curepto'),
        (189, 'Empedrado'),
        (190, 'Maule'),
        (191, 'Pelarco'),
        (192, 'Pencahue'),
        (193, 'Río Claro'),
        (194, 'San Clemente'),
        (195, 'San Rafael'),
        (196, 'Talca'),
        (197, 'Arauco'),
        (198, 'Cañete'),
        (199, 'Contulmo'),
        (200, 'Curanilahue'),
        (201, 'Lebu'),
        (202, 'Los Álamos'),
        (203, 'Tirúa'),
        (204, 'Alto Biobío'),
        (205, 'Antuco'),
        (206, 'Cabrero'),
        (207, 'Laja'),
        (208, 'Los Ángeles'),
        (209, 'Mulchén'),
        (210, 'Nacimiento'),
        (211, 'Negrete'),
        (212, 'Quilaco'),
        (213, 'Quilleco'),
        (214, 'San Rosendo'),
        (215, 'Santa Bárbara'),
        (216, 'Tucapel'),
        (217, 'Yumbel'),
        (218, 'Chiguayante'),
        (219, 'Concepción'),
        (220, 'Coronel'),
        (221, 'Florida'),
        (222, 'Hualpén'),
        (223, 'Hualqui'),
        (224, 'Lota'),
        (225, 'Penco'),
        (226, 'San Pedro de La Paz'),
        (227, 'Santa Juana'),
        (228, 'Talcahuano'),
        (229, 'Tomé'),
        (230, 'Bulnes'),
        (231, 'Chillán'),
        (232, 'Chillán Viejo'),
        (233, 'Cobquecura'),
        (234, 'Coelemu'),
        (235, 'Coihueco'),
        (236, 'El Carmen'),
        (237, 'Ninhue'),
        (238, 'Ñiquen'),
        (239, 'Pemuco'),
        (240, 'Pinto'),
        (241, 'Portezuelo'),
        (242, 'Quillón'),
        (243, 'Quirihue'),
        (244, 'Ránquil'),
        (245, 'San Carlos'),
        (246, 'San Fabián'),
        (247, 'San Ignacio'),
        (248, 'San Nicolás'),
        (249, 'Treguaco'),
        (250, 'Yungay'),
        (251, 'Carahue'),
        (252, 'Cholchol'),
        (253, 'Cunco'),
        (254, 'Curarrehue'),
        (255, 'Freire'),
        (256, 'Galvarino'),
        (257, 'Gorbea'),
        (258, 'Lautaro'),
        (259, 'Loncoche'),
        (260, 'Melipeuco'),
        (261, 'Nueva Imperial'),
        (262, 'Padre Las Casas'),
        (263, 'Perquenco'),
        (264, 'Pitrufquén'),
        (265, 'Pucón'),
        (266, 'Saavedra'),
        (267, 'Temuco'),
        (268, 'Teodoro Schmidt'),
        (269, 'Toltén'),
        (270, 'Vilcún'),
        (271, 'Villarrica'),
        (272, 'Angol'),
        (273, 'Collipulli'),
        (274, 'Curacautín'),
        (275, 'Ercilla'),
        (276, 'Lonquimay'),
        (277, 'Los Sauces'),
        (278, 'Lumaco'),
        (279, 'Purén'),
        (280, 'Renaico'),
        (281, 'Traiguén'),
        (282, 'Victoria'),
        (283, 'Corral'),
        (284, 'Lanco'),
        (285, 'Los Lagos'),
        (286, 'Máfil'),
        (287, 'Mariquina'),
        (288, 'Paillaco'),
        (289, 'Panguipulli'),
        (290, 'Valdivia'),
        (291, 'Futrono'),
        (292, 'La Unión'),
        (293, 'Lago Ranco'),
        (294, 'Río Bueno'),
        (295, 'Ancud'),
        (296, 'Castro'),
        (297, 'Chonchi'),
        (298, 'Curaco de Vélez'),
        (299, 'Dalcahue'),
        (300, 'Puqueldón'),
        (301, 'Queilén'),
        (302, 'Quemchi'),
        (303, 'Quellón'),
        (304, 'Quinchao'),
        (305, 'Calbuco'),
        (306, 'Cochamó'),
        (307, 'Fresia'),
        (308, 'Frutillar'),
        (309, 'Llanquihue'),
        (310, 'Los Muermos'),
        (311, 'Maullín'),
        (312, 'Puerto Montt'),
        (313, 'Puerto Varas'),
        (314, 'Osorno'),
        (315, 'Puerto Octay'),
        (316, 'Purranque'),
        (317, 'Puyehue'),
        (318, 'Río Negro'),
        (319, 'San Juan de la Costa'),
        (320, 'San Pablo'),
        (321, 'Chaitén'),
        (322, 'Futaleufú'),
        (323, 'Hualaihué'),
        (324, 'Palena'),
        (325, 'Aysén'),
        (326, 'Cisnes'),
        (327, 'Guaitecas'),
        (328, 'Cochrane'),
        (329, 'Ohiggins'),
        (330, 'Tortel'),
        (331, 'Coyhaique'),
        (332, 'Lago Verde'),
        (333, 'Chile Chico'),
        (334, 'Río Ibáñez'),
        (335, 'Antártica'),
        (336, 'Cabo de Hornos'),
        (337, 'Laguna Blanca'),
        (338, 'Punta Arenas'),
        (339, 'Río Verde'),
        (340, 'San Gregorio'),
        (341, 'Porvenir'),
        (342, 'Primavera'),
        (343, 'Timaukel'),
        (344, 'Natales'),
        (345, 'Torres del Paine'),
        (346, 'Cabildo'), ]
    return comuna
