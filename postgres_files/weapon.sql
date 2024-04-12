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
-- Name: dndinventory_weapon; Type: TABLE; Schema: public; Owner: django
--

CREATE TABLE public.dndinventory_weapon (
    equipment_id bigint NOT NULL,
    die_rolls smallint NOT NULL,
    damage_die smallint NOT NULL,
    strength boolean NOT NULL,
    dexterity boolean NOT NULL
);


ALTER TABLE public.dndinventory_weapon OWNER TO django;

--
-- Data for Name: dndinventory_weapon; Type: TABLE DATA; Schema: public; Owner: django
--

COPY public.dndinventory_weapon (equipment_id, die_rolls, damage_die, strength, dexterity) FROM stdin;
2	1	4	t	f
5	0	1	f	t
1	1	4	t	f
4	0	0	f	t
\.


--
-- Name: dndinventory_weapon dndinventory_weapon_pkey; Type: CONSTRAINT; Schema: public; Owner: django
--

ALTER TABLE ONLY public.dndinventory_weapon
    ADD CONSTRAINT dndinventory_weapon_pkey PRIMARY KEY (equipment_id);


--
-- Name: dndinventory_weapon dndinventory_weapon_equipment_id_e45d3074_fk_dndinvent; Type: FK CONSTRAINT; Schema: public; Owner: django
--

ALTER TABLE ONLY public.dndinventory_weapon
    ADD CONSTRAINT dndinventory_weapon_equipment_id_e45d3074_fk_dndinvent FOREIGN KEY (equipment_id) REFERENCES public.dndinventory_equipment(id) DEFERRABLE INITIALLY DEFERRED;


--
-- PostgreSQL database dump complete
--

