--
-- PostgreSQL database dump
--

-- Dumped from database version 16.1 (Debian 16.1-1.pgdg120+1)
-- Dumped by pg_dump version 16.1 (Debian 16.1-1.pgdg120+1)

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: dndinventory_equipmentproperty; Type: TABLE; Schema: public; Owner: django
--

CREATE TABLE public.dndinventory_equipmentproperty (
    id integer NOT NULL,
    property character varying(20) NOT NULL,
    value character varying(20),
    equipment_id bigint NOT NULL
);


ALTER TABLE public.dndinventory_equipmentproperty OWNER TO django;

--
-- Name: dndinventory_equipmentproperty_id_seq; Type: SEQUENCE; Schema: public; Owner: django
--

ALTER TABLE public.dndinventory_equipmentproperty ALTER COLUMN id ADD GENERATED BY DEFAULT AS IDENTITY (
    SEQUENCE NAME public.dndinventory_equipmentproperty_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- Data for Name: dndinventory_equipmentproperty; Type: TABLE DATA; Schema: public; Owner: django
--

COPY public.dndinventory_equipmentproperty (id, property, value, equipment_id) FROM stdin;
1	Light	\N	1
2	Light	\N	2
3	Thrown	\N	2
4	Thrown	\N	3
5	Thrown	\N	4
6	Ammunition	\N	5
7	Poison	Ingested	240
8	Poison	Inhaled	241
9	Poison	Contact	242
10	Poison	Injury	243
11	Poison	Inhaled	244
12	Poison	Inhaled	245
13	Poison	Ingested	246
14	Poison	Contact	247
15	Poison	Ingested	248
16	Poison	Injury	249
17	Poison	Injury	250
18	Poison	Ingested	251
19	Poison	Ingested	252
20	Poison	Injury	253
21	Thrown	\N	120
22	Finesse	\N	120
23	Range	20	120
24	Long Range	60	120
25	Two-Handed	\N	121
26	Light	\N	122
\.


--
-- Name: dndinventory_equipmentproperty_id_seq; Type: SEQUENCE SET; Schema: public; Owner: django
--

SELECT pg_catalog.setval('public.dndinventory_equipmentproperty_id_seq', 26, true);


--
-- Name: dndinventory_equipmentproperty combination_equipment_property; Type: CONSTRAINT; Schema: public; Owner: django
--

ALTER TABLE ONLY public.dndinventory_equipmentproperty
    ADD CONSTRAINT combination_equipment_property UNIQUE (equipment_id, property);


--
-- Name: dndinventory_equipmentproperty dndinventory_equipmentproperty_pkey; Type: CONSTRAINT; Schema: public; Owner: django
--

ALTER TABLE ONLY public.dndinventory_equipmentproperty
    ADD CONSTRAINT dndinventory_equipmentproperty_pkey PRIMARY KEY (id);


--
-- Name: dndinventory_equipmentproperty_equipment_id_c544a7c0; Type: INDEX; Schema: public; Owner: django
--

CREATE INDEX dndinventory_equipmentproperty_equipment_id_c544a7c0 ON public.dndinventory_equipmentproperty USING btree (equipment_id);


--
-- Name: dndinventory_equipmentproperty dndinventory_equipme_equipment_id_c544a7c0_fk_dndinvent; Type: FK CONSTRAINT; Schema: public; Owner: django
--

ALTER TABLE ONLY public.dndinventory_equipmentproperty
    ADD CONSTRAINT dndinventory_equipme_equipment_id_c544a7c0_fk_dndinvent FOREIGN KEY (equipment_id) REFERENCES public.dndinventory_equipment(id) DEFERRABLE INITIALLY DEFERRED;


--
-- PostgreSQL database dump complete
--
