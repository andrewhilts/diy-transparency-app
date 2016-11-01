--
-- PostgreSQL database dump
--

SET statement_timeout = 0;
SET lock_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SET check_function_bodies = false;
SET client_min_messages = warning;

SET search_path = public, pg_catalog;

ALTER TABLE ONLY public.type_disclosure_responses DROP CONSTRAINT type_disclosure_responses_response_id_fkey;
ALTER TABLE ONLY public.type_disclosure_responses DROP CONSTRAINT type_disclosure_responses_disclosure_id_fkey;
ALTER TABLE ONLY public.law_enforcement_handbooks DROP CONSTRAINT law_enforcement_handbooks_transparency_report_id_fkey;
ALTER TABLE ONLY public.law_enforcement_actions DROP CONSTRAINT law_enforcement_actions_category_id_fkey;
ALTER TABLE ONLY public.law_enfocement_handbook_actions DROP CONSTRAINT law_enfocement_handbook_actions_handbook_id_fkey;
ALTER TABLE ONLY public.law_enfocement_handbook_actions DROP CONSTRAINT law_enfocement_handbook_actions_handbook_category_id_fkey;
ALTER TABLE ONLY public.law_enfocement_handbook_actions DROP CONSTRAINT law_enfocement_handbook_actions_action_id_fkey;
ALTER TABLE ONLY public.law_enfocement_handbook_action_categories DROP CONSTRAINT law_enfocement_handbook_action_categories_handbook_id_fkey;
ALTER TABLE ONLY public.law_enfocement_handbook_action_categories DROP CONSTRAINT law_enfocement_handbook_action_categori_action_category_id_fkey;
ALTER TABLE ONLY public.government_requests_reports DROP CONSTRAINT government_requests_reports_transparency_report_id_fkey;
ALTER TABLE ONLY public.government_request_types DROP CONSTRAINT government_request_types_category_id_fkey;
ALTER TABLE ONLY public.government_request_report_type_disclosures DROP CONSTRAINT government_request_report_type_disclosures_request_type_id_fkey;
ALTER TABLE ONLY public.government_request_report_type_disclosures DROP CONSTRAINT government_request_report_type_disclosur_request_report_id_fkey;
ALTER TABLE ONLY public.data_retention_guides DROP CONSTRAINT data_retention_guides_transparency_report_id_fkey;
ALTER TABLE ONLY public.data_retention_guide_items DROP CONSTRAINT data_retention_guide_items_guide_id_fkey;
ALTER TABLE ONLY public.data_retention_guide_items DROP CONSTRAINT data_retention_guide_items_guide_data_item_id_fkey;
ALTER TABLE ONLY public.data_retention_guide_items DROP CONSTRAINT data_retention_guide_items_guide_category_id_fkey;
ALTER TABLE ONLY public.data_retention_guide_categories DROP CONSTRAINT data_retention_guide_categories_guide_id_fkey;
ALTER TABLE ONLY public.data_retention_guide_categories DROP CONSTRAINT data_retention_guide_categories_guide_data_category_id_fkey;
ALTER TABLE ONLY public.data_items DROP CONSTRAINT data_items_category_id_fkey;
ALTER TABLE ONLY public.type_disclosure_responses DROP CONSTRAINT type_disclosure_responses_pkey;
ALTER TABLE ONLY public.transparency_reports DROP CONSTRAINT transparency_reports_pkey;
ALTER TABLE ONLY public.law_enforcement_handbooks DROP CONSTRAINT law_enforcement_handbooks_pkey;
ALTER TABLE ONLY public.law_enforcement_actions DROP CONSTRAINT law_enforcement_actions_pkey;
ALTER TABLE ONLY public.law_enforcement_action_categories DROP CONSTRAINT law_enforcement_action_categories_pkey;
ALTER TABLE ONLY public.law_enfocement_handbook_actions DROP CONSTRAINT law_enfocement_handbook_actions_pkey;
ALTER TABLE ONLY public.law_enfocement_handbook_action_categories DROP CONSTRAINT law_enfocement_handbook_action_categories_pkey;
ALTER TABLE ONLY public.government_requests_reports DROP CONSTRAINT government_requests_reports_pkey;
ALTER TABLE ONLY public.government_request_types DROP CONSTRAINT government_request_types_pkey;
ALTER TABLE ONLY public.government_request_responses DROP CONSTRAINT government_request_responses_pkey;
ALTER TABLE ONLY public.government_request_report_type_disclosures DROP CONSTRAINT government_request_report_type_disclosures_pkey;
ALTER TABLE ONLY public.government_request_categories DROP CONSTRAINT government_request_categories_pkey;
ALTER TABLE ONLY public.data_retention_guides DROP CONSTRAINT data_retention_guides_pkey;
ALTER TABLE ONLY public.data_retention_guide_items DROP CONSTRAINT data_retention_guide_items_pkey;
ALTER TABLE ONLY public.data_retention_guide_categories DROP CONSTRAINT data_retention_guide_categories_pkey;
ALTER TABLE ONLY public.data_items DROP CONSTRAINT data_items_pkey;
ALTER TABLE ONLY public.data_categories DROP CONSTRAINT data_categories_pkey;
ALTER TABLE public.type_disclosure_responses ALTER COLUMN type_disclosure_id DROP DEFAULT;
ALTER TABLE public.transparency_reports ALTER COLUMN report_id DROP DEFAULT;
ALTER TABLE public.law_enforcement_handbooks ALTER COLUMN handbook_id DROP DEFAULT;
ALTER TABLE public.law_enforcement_actions ALTER COLUMN action_id DROP DEFAULT;
ALTER TABLE public.law_enforcement_action_categories ALTER COLUMN category_id DROP DEFAULT;
ALTER TABLE public.law_enfocement_handbook_actions ALTER COLUMN handbook_action_id DROP DEFAULT;
ALTER TABLE public.law_enfocement_handbook_action_categories ALTER COLUMN handbook_category_id DROP DEFAULT;
ALTER TABLE public.government_requests_reports ALTER COLUMN report_id DROP DEFAULT;
ALTER TABLE public.government_request_types ALTER COLUMN type_id DROP DEFAULT;
ALTER TABLE public.government_request_responses ALTER COLUMN response_id DROP DEFAULT;
ALTER TABLE public.government_request_report_type_disclosures ALTER COLUMN disclosure_id DROP DEFAULT;
ALTER TABLE public.government_request_categories ALTER COLUMN category_id DROP DEFAULT;
ALTER TABLE public.data_retention_guides ALTER COLUMN guide_id DROP DEFAULT;
ALTER TABLE public.data_retention_guide_items ALTER COLUMN guide_item_id DROP DEFAULT;
ALTER TABLE public.data_retention_guide_categories ALTER COLUMN guide_category_id DROP DEFAULT;
ALTER TABLE public.data_items ALTER COLUMN item_id DROP DEFAULT;
ALTER TABLE public.data_categories ALTER COLUMN category_id DROP DEFAULT;
DROP SEQUENCE public.type_disclosure_responses_type_disclosure_id_seq;
DROP TABLE public.type_disclosure_responses;
DROP SEQUENCE public.transparency_reports_report_id_seq;
DROP TABLE public.transparency_reports;
DROP SEQUENCE public.law_enforcement_handbooks_handbook_id_seq;
DROP TABLE public.law_enforcement_handbooks;
DROP SEQUENCE public.law_enforcement_actions_action_id_seq;
DROP TABLE public.law_enforcement_actions;
DROP SEQUENCE public.law_enforcement_action_categories_category_id_seq;
DROP TABLE public.law_enforcement_action_categories;
DROP SEQUENCE public.law_enfocement_handbook_actions_handbook_action_id_seq;
DROP TABLE public.law_enfocement_handbook_actions;
DROP SEQUENCE public.law_enfocement_handbook_action_categor_handbook_category_id_seq;
DROP TABLE public.law_enfocement_handbook_action_categories;
DROP SEQUENCE public.government_requests_reports_report_id_seq;
DROP TABLE public.government_requests_reports;
DROP SEQUENCE public.government_request_types_type_id_seq;
DROP TABLE public.government_request_types;
DROP SEQUENCE public.government_request_responses_response_id_seq;
DROP TABLE public.government_request_responses;
DROP SEQUENCE public.government_request_report_type_disclosures_disclosure_id_seq;
DROP TABLE public.government_request_report_type_disclosures;
DROP SEQUENCE public.government_request_categories_category_id_seq;
DROP TABLE public.government_request_categories;
DROP SEQUENCE public.data_retention_guides_guide_id_seq;
DROP TABLE public.data_retention_guides;
DROP SEQUENCE public.data_retention_guide_items_guide_item_id_seq;
DROP TABLE public.data_retention_guide_items;
DROP SEQUENCE public.data_retention_guide_categories_guide_category_id_seq;
DROP TABLE public.data_retention_guide_categories;
DROP SEQUENCE public.data_items_item_id_seq;
DROP TABLE public.data_items;
DROP SEQUENCE public.data_categories_category_id_seq;
DROP TABLE public.data_categories;
DROP EXTENSION plpgsql;
DROP SCHEMA public;
--
-- Name: public; Type: SCHEMA; Schema: -; Owner: postgres
--

CREATE SCHEMA public;


ALTER SCHEMA public OWNER TO postgres;

--
-- Name: SCHEMA public; Type: COMMENT; Schema: -; Owner: postgres
--

COMMENT ON SCHEMA public IS 'standard public schema';


--
-- Name: plpgsql; Type: EXTENSION; Schema: -; Owner: 
--

CREATE EXTENSION IF NOT EXISTS plpgsql WITH SCHEMA pg_catalog;


--
-- Name: EXTENSION plpgsql; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION plpgsql IS 'PL/pgSQL procedural language';


SET search_path = public, pg_catalog;

SET default_tablespace = '';

SET default_with_oids = false;

--
-- Name: data_categories; Type: TABLE; Schema: public; Owner: transdb; Tablespace: 
--

CREATE TABLE data_categories (
    category_id integer NOT NULL,
    name character varying(255),
    description text
);


ALTER TABLE public.data_categories OWNER TO transdb;

--
-- Name: data_categories_category_id_seq; Type: SEQUENCE; Schema: public; Owner: transdb
--

CREATE SEQUENCE data_categories_category_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.data_categories_category_id_seq OWNER TO transdb;

--
-- Name: data_categories_category_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: transdb
--

ALTER SEQUENCE data_categories_category_id_seq OWNED BY data_categories.category_id;


--
-- Name: data_items; Type: TABLE; Schema: public; Owner: transdb; Tablespace: 
--

CREATE TABLE data_items (
    item_id integer NOT NULL,
    name character varying(255),
    description text,
    category_id integer
);


ALTER TABLE public.data_items OWNER TO transdb;

--
-- Name: data_items_item_id_seq; Type: SEQUENCE; Schema: public; Owner: transdb
--

CREATE SEQUENCE data_items_item_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.data_items_item_id_seq OWNER TO transdb;

--
-- Name: data_items_item_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: transdb
--

ALTER SEQUENCE data_items_item_id_seq OWNED BY data_items.item_id;


--
-- Name: data_retention_guide_categories; Type: TABLE; Schema: public; Owner: transdb; Tablespace: 
--

CREATE TABLE data_retention_guide_categories (
    guide_id integer NOT NULL,
    guide_data_category_id integer NOT NULL,
    inclusion_status boolean,
    retention_status boolean,
    guide_category_id integer NOT NULL
);


ALTER TABLE public.data_retention_guide_categories OWNER TO transdb;

--
-- Name: data_retention_guide_categories_guide_category_id_seq; Type: SEQUENCE; Schema: public; Owner: transdb
--

CREATE SEQUENCE data_retention_guide_categories_guide_category_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.data_retention_guide_categories_guide_category_id_seq OWNER TO transdb;

--
-- Name: data_retention_guide_categories_guide_category_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: transdb
--

ALTER SEQUENCE data_retention_guide_categories_guide_category_id_seq OWNED BY data_retention_guide_categories.guide_category_id;


--
-- Name: data_retention_guide_items; Type: TABLE; Schema: public; Owner: transdb; Tablespace: 
--

CREATE TABLE data_retention_guide_items (
    guide_id integer NOT NULL,
    guide_data_item_id integer NOT NULL,
    narrative text,
    inclusion_status boolean,
    retention_status boolean,
    guide_item_id integer NOT NULL,
    guide_category_id integer,
    retention_period integer,
    retention_period_unit integer
);


ALTER TABLE public.data_retention_guide_items OWNER TO transdb;

--
-- Name: data_retention_guide_items_guide_item_id_seq; Type: SEQUENCE; Schema: public; Owner: transdb
--

CREATE SEQUENCE data_retention_guide_items_guide_item_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.data_retention_guide_items_guide_item_id_seq OWNER TO transdb;

--
-- Name: data_retention_guide_items_guide_item_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: transdb
--

ALTER SEQUENCE data_retention_guide_items_guide_item_id_seq OWNED BY data_retention_guide_items.guide_item_id;


--
-- Name: data_retention_guides; Type: TABLE; Schema: public; Owner: transdb; Tablespace: 
--

CREATE TABLE data_retention_guides (
    guide_id integer NOT NULL,
    inclusion_status boolean,
    complete_status boolean,
    narrative text,
    transparency_report_id integer,
    date_updated date
);


ALTER TABLE public.data_retention_guides OWNER TO transdb;

--
-- Name: data_retention_guides_guide_id_seq; Type: SEQUENCE; Schema: public; Owner: transdb
--

CREATE SEQUENCE data_retention_guides_guide_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.data_retention_guides_guide_id_seq OWNER TO transdb;

--
-- Name: data_retention_guides_guide_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: transdb
--

ALTER SEQUENCE data_retention_guides_guide_id_seq OWNED BY data_retention_guides.guide_id;


--
-- Name: government_request_categories; Type: TABLE; Schema: public; Owner: transdb; Tablespace: 
--

CREATE TABLE government_request_categories (
    category_id integer NOT NULL,
    name character varying(255),
    description text
);


ALTER TABLE public.government_request_categories OWNER TO transdb;

--
-- Name: government_request_categories_category_id_seq; Type: SEQUENCE; Schema: public; Owner: transdb
--

CREATE SEQUENCE government_request_categories_category_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.government_request_categories_category_id_seq OWNER TO transdb;

--
-- Name: government_request_categories_category_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: transdb
--

ALTER SEQUENCE government_request_categories_category_id_seq OWNED BY government_request_categories.category_id;


--
-- Name: government_request_report_type_disclosures; Type: TABLE; Schema: public; Owner: transdb; Tablespace: 
--

CREATE TABLE government_request_report_type_disclosures (
    disclosure_id integer NOT NULL,
    request_report_id integer,
    request_type_id integer
);


ALTER TABLE public.government_request_report_type_disclosures OWNER TO transdb;

--
-- Name: government_request_report_type_disclosures_disclosure_id_seq; Type: SEQUENCE; Schema: public; Owner: transdb
--

CREATE SEQUENCE government_request_report_type_disclosures_disclosure_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.government_request_report_type_disclosures_disclosure_id_seq OWNER TO transdb;

--
-- Name: government_request_report_type_disclosures_disclosure_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: transdb
--

ALTER SEQUENCE government_request_report_type_disclosures_disclosure_id_seq OWNED BY government_request_report_type_disclosures.disclosure_id;


--
-- Name: government_request_responses; Type: TABLE; Schema: public; Owner: transdb; Tablespace: 
--

CREATE TABLE government_request_responses (
    response_id integer NOT NULL,
    name character varying(255),
    description text
);


ALTER TABLE public.government_request_responses OWNER TO transdb;

--
-- Name: government_request_responses_response_id_seq; Type: SEQUENCE; Schema: public; Owner: transdb
--

CREATE SEQUENCE government_request_responses_response_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.government_request_responses_response_id_seq OWNER TO transdb;

--
-- Name: government_request_responses_response_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: transdb
--

ALTER SEQUENCE government_request_responses_response_id_seq OWNED BY government_request_responses.response_id;


--
-- Name: government_request_types; Type: TABLE; Schema: public; Owner: transdb; Tablespace: 
--

CREATE TABLE government_request_types (
    type_id integer NOT NULL,
    category_id integer,
    name character varying(255),
    description text
);


ALTER TABLE public.government_request_types OWNER TO transdb;

--
-- Name: government_request_types_type_id_seq; Type: SEQUENCE; Schema: public; Owner: transdb
--

CREATE SEQUENCE government_request_types_type_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.government_request_types_type_id_seq OWNER TO transdb;

--
-- Name: government_request_types_type_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: transdb
--

ALTER SEQUENCE government_request_types_type_id_seq OWNED BY government_request_types.type_id;


--
-- Name: government_requests_reports; Type: TABLE; Schema: public; Owner: transdb; Tablespace: 
--

CREATE TABLE government_requests_reports (
    report_id integer NOT NULL,
    transparency_report_id integer,
    inclusion_status boolean,
    complete_status boolean,
    narrative text,
    date_updated date
);


ALTER TABLE public.government_requests_reports OWNER TO transdb;

--
-- Name: government_requests_reports_report_id_seq; Type: SEQUENCE; Schema: public; Owner: transdb
--

CREATE SEQUENCE government_requests_reports_report_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.government_requests_reports_report_id_seq OWNER TO transdb;

--
-- Name: government_requests_reports_report_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: transdb
--

ALTER SEQUENCE government_requests_reports_report_id_seq OWNED BY government_requests_reports.report_id;


--
-- Name: law_enfocement_handbook_action_categories; Type: TABLE; Schema: public; Owner: transdb; Tablespace: 
--

CREATE TABLE law_enfocement_handbook_action_categories (
    handbook_id integer NOT NULL,
    action_category_id integer NOT NULL,
    inclusion_status boolean,
    handbook_category_id integer NOT NULL
);


ALTER TABLE public.law_enfocement_handbook_action_categories OWNER TO transdb;

--
-- Name: law_enfocement_handbook_action_categor_handbook_category_id_seq; Type: SEQUENCE; Schema: public; Owner: transdb
--

CREATE SEQUENCE law_enfocement_handbook_action_categor_handbook_category_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.law_enfocement_handbook_action_categor_handbook_category_id_seq OWNER TO transdb;

--
-- Name: law_enfocement_handbook_action_categor_handbook_category_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: transdb
--

ALTER SEQUENCE law_enfocement_handbook_action_categor_handbook_category_id_seq OWNED BY law_enfocement_handbook_action_categories.handbook_category_id;


--
-- Name: law_enfocement_handbook_actions; Type: TABLE; Schema: public; Owner: transdb; Tablespace: 
--

CREATE TABLE law_enfocement_handbook_actions (
    handbook_id integer NOT NULL,
    action_id integer NOT NULL,
    narrative text,
    inclusion_status boolean,
    handbook_category_id integer,
    handbook_action_id integer NOT NULL
);


ALTER TABLE public.law_enfocement_handbook_actions OWNER TO transdb;

--
-- Name: law_enfocement_handbook_actions_handbook_action_id_seq; Type: SEQUENCE; Schema: public; Owner: transdb
--

CREATE SEQUENCE law_enfocement_handbook_actions_handbook_action_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.law_enfocement_handbook_actions_handbook_action_id_seq OWNER TO transdb;

--
-- Name: law_enfocement_handbook_actions_handbook_action_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: transdb
--

ALTER SEQUENCE law_enfocement_handbook_actions_handbook_action_id_seq OWNED BY law_enfocement_handbook_actions.handbook_action_id;


--
-- Name: law_enforcement_action_categories; Type: TABLE; Schema: public; Owner: transdb; Tablespace: 
--

CREATE TABLE law_enforcement_action_categories (
    category_id integer NOT NULL,
    name character varying(255),
    action_selection_type integer,
    description text
);


ALTER TABLE public.law_enforcement_action_categories OWNER TO transdb;

--
-- Name: law_enforcement_action_categories_category_id_seq; Type: SEQUENCE; Schema: public; Owner: transdb
--

CREATE SEQUENCE law_enforcement_action_categories_category_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.law_enforcement_action_categories_category_id_seq OWNER TO transdb;

--
-- Name: law_enforcement_action_categories_category_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: transdb
--

ALTER SEQUENCE law_enforcement_action_categories_category_id_seq OWNED BY law_enforcement_action_categories.category_id;


--
-- Name: law_enforcement_actions; Type: TABLE; Schema: public; Owner: transdb; Tablespace: 
--

CREATE TABLE law_enforcement_actions (
    action_id integer NOT NULL,
    category_id integer,
    name character varying(255),
    narrative text,
    narrative_label character varying(255),
    inclusion_status_default boolean
);


ALTER TABLE public.law_enforcement_actions OWNER TO transdb;

--
-- Name: law_enforcement_actions_action_id_seq; Type: SEQUENCE; Schema: public; Owner: transdb
--

CREATE SEQUENCE law_enforcement_actions_action_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.law_enforcement_actions_action_id_seq OWNER TO transdb;

--
-- Name: law_enforcement_actions_action_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: transdb
--

ALTER SEQUENCE law_enforcement_actions_action_id_seq OWNED BY law_enforcement_actions.action_id;


--
-- Name: law_enforcement_handbooks; Type: TABLE; Schema: public; Owner: transdb; Tablespace: 
--

CREATE TABLE law_enforcement_handbooks (
    handbook_id integer NOT NULL,
    inclusion_status boolean,
    complete_status boolean,
    narrative text,
    date_updated date,
    date_updated_inclusion_status boolean,
    transparency_report_id integer
);


ALTER TABLE public.law_enforcement_handbooks OWNER TO transdb;

--
-- Name: law_enforcement_handbooks_handbook_id_seq; Type: SEQUENCE; Schema: public; Owner: transdb
--

CREATE SEQUENCE law_enforcement_handbooks_handbook_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.law_enforcement_handbooks_handbook_id_seq OWNER TO transdb;

--
-- Name: law_enforcement_handbooks_handbook_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: transdb
--

ALTER SEQUENCE law_enforcement_handbooks_handbook_id_seq OWNED BY law_enforcement_handbooks.handbook_id;


--
-- Name: transparency_reports; Type: TABLE; Schema: public; Owner: transdb; Tablespace: 
--

CREATE TABLE transparency_reports (
    report_id integer NOT NULL,
    publication_status boolean,
    complete_status boolean,
    publication_date date,
    report_period_start date,
    report_period_end date,
    author_name character varying(255),
    date_updated date
);


ALTER TABLE public.transparency_reports OWNER TO transdb;

--
-- Name: transparency_reports_report_id_seq; Type: SEQUENCE; Schema: public; Owner: transdb
--

CREATE SEQUENCE transparency_reports_report_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.transparency_reports_report_id_seq OWNER TO transdb;

--
-- Name: transparency_reports_report_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: transdb
--

ALTER SEQUENCE transparency_reports_report_id_seq OWNED BY transparency_reports.report_id;


--
-- Name: type_disclosure_responses; Type: TABLE; Schema: public; Owner: transdb; Tablespace: 
--

CREATE TABLE type_disclosure_responses (
    response_id integer NOT NULL,
    disclosure_id integer NOT NULL,
    count integer,
    type_disclosure_id integer NOT NULL
);


ALTER TABLE public.type_disclosure_responses OWNER TO transdb;

--
-- Name: type_disclosure_responses_type_disclosure_id_seq; Type: SEQUENCE; Schema: public; Owner: transdb
--

CREATE SEQUENCE type_disclosure_responses_type_disclosure_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.type_disclosure_responses_type_disclosure_id_seq OWNER TO transdb;

--
-- Name: type_disclosure_responses_type_disclosure_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: transdb
--

ALTER SEQUENCE type_disclosure_responses_type_disclosure_id_seq OWNED BY type_disclosure_responses.type_disclosure_id;


--
-- Name: category_id; Type: DEFAULT; Schema: public; Owner: transdb
--

ALTER TABLE ONLY data_categories ALTER COLUMN category_id SET DEFAULT nextval('data_categories_category_id_seq'::regclass);


--
-- Name: item_id; Type: DEFAULT; Schema: public; Owner: transdb
--

ALTER TABLE ONLY data_items ALTER COLUMN item_id SET DEFAULT nextval('data_items_item_id_seq'::regclass);


--
-- Name: guide_category_id; Type: DEFAULT; Schema: public; Owner: transdb
--

ALTER TABLE ONLY data_retention_guide_categories ALTER COLUMN guide_category_id SET DEFAULT nextval('data_retention_guide_categories_guide_category_id_seq'::regclass);


--
-- Name: guide_item_id; Type: DEFAULT; Schema: public; Owner: transdb
--

ALTER TABLE ONLY data_retention_guide_items ALTER COLUMN guide_item_id SET DEFAULT nextval('data_retention_guide_items_guide_item_id_seq'::regclass);


--
-- Name: guide_id; Type: DEFAULT; Schema: public; Owner: transdb
--

ALTER TABLE ONLY data_retention_guides ALTER COLUMN guide_id SET DEFAULT nextval('data_retention_guides_guide_id_seq'::regclass);


--
-- Name: category_id; Type: DEFAULT; Schema: public; Owner: transdb
--

ALTER TABLE ONLY government_request_categories ALTER COLUMN category_id SET DEFAULT nextval('government_request_categories_category_id_seq'::regclass);


--
-- Name: disclosure_id; Type: DEFAULT; Schema: public; Owner: transdb
--

ALTER TABLE ONLY government_request_report_type_disclosures ALTER COLUMN disclosure_id SET DEFAULT nextval('government_request_report_type_disclosures_disclosure_id_seq'::regclass);


--
-- Name: response_id; Type: DEFAULT; Schema: public; Owner: transdb
--

ALTER TABLE ONLY government_request_responses ALTER COLUMN response_id SET DEFAULT nextval('government_request_responses_response_id_seq'::regclass);


--
-- Name: type_id; Type: DEFAULT; Schema: public; Owner: transdb
--

ALTER TABLE ONLY government_request_types ALTER COLUMN type_id SET DEFAULT nextval('government_request_types_type_id_seq'::regclass);


--
-- Name: report_id; Type: DEFAULT; Schema: public; Owner: transdb
--

ALTER TABLE ONLY government_requests_reports ALTER COLUMN report_id SET DEFAULT nextval('government_requests_reports_report_id_seq'::regclass);


--
-- Name: handbook_category_id; Type: DEFAULT; Schema: public; Owner: transdb
--

ALTER TABLE ONLY law_enfocement_handbook_action_categories ALTER COLUMN handbook_category_id SET DEFAULT nextval('law_enfocement_handbook_action_categor_handbook_category_id_seq'::regclass);


--
-- Name: handbook_action_id; Type: DEFAULT; Schema: public; Owner: transdb
--

ALTER TABLE ONLY law_enfocement_handbook_actions ALTER COLUMN handbook_action_id SET DEFAULT nextval('law_enfocement_handbook_actions_handbook_action_id_seq'::regclass);


--
-- Name: category_id; Type: DEFAULT; Schema: public; Owner: transdb
--

ALTER TABLE ONLY law_enforcement_action_categories ALTER COLUMN category_id SET DEFAULT nextval('law_enforcement_action_categories_category_id_seq'::regclass);


--
-- Name: action_id; Type: DEFAULT; Schema: public; Owner: transdb
--

ALTER TABLE ONLY law_enforcement_actions ALTER COLUMN action_id SET DEFAULT nextval('law_enforcement_actions_action_id_seq'::regclass);


--
-- Name: handbook_id; Type: DEFAULT; Schema: public; Owner: transdb
--

ALTER TABLE ONLY law_enforcement_handbooks ALTER COLUMN handbook_id SET DEFAULT nextval('law_enforcement_handbooks_handbook_id_seq'::regclass);


--
-- Name: report_id; Type: DEFAULT; Schema: public; Owner: transdb
--

ALTER TABLE ONLY transparency_reports ALTER COLUMN report_id SET DEFAULT nextval('transparency_reports_report_id_seq'::regclass);


--
-- Name: type_disclosure_id; Type: DEFAULT; Schema: public; Owner: transdb
--

ALTER TABLE ONLY type_disclosure_responses ALTER COLUMN type_disclosure_id SET DEFAULT nextval('type_disclosure_responses_type_disclosure_id_seq'::regclass);


--
-- Data for Name: data_categories; Type: TABLE DATA; Schema: public; Owner: transdb
--

COPY data_categories (category_id, name, description) FROM stdin;
5	Personally Identifiable Information	Personal information means information about an identifiable individual. Canadian court decisions mean that this definition should be given a broad an expansive interpretation. In part, this means that information about an individual can merely relate to an individual, that information can be personal while simultaneously pertaining to more than just one person, that even public information can be personal, and that what is often core to the definition is that an individual is identifiable by way of the information, even if they are not identified using it.
6	Content	Content information refers to data which discloses the explicit meaning of a conversation, such as contents of files or communications.
4	Subscriber Data	Subscriber data refers to that collected by organizations, or provided by individuals voluntarily, in the course of signing up for accounts or fulfilling services or product orders.
19	Transmission Data	Transmission data orders are obtained using a transmission data recorder order, as denoted under s.492.2 of the Criminal Code. These orders are used to obtain data that is obtained by dialling, addressing, routing, or signalling, such as incoming and outgoing times of calls, non-content information associated with text messages or chat-based communications, or other data that does not reveal the content of the communication or message. Transmission data is more commonly known as 'metadata'.
24	New Category type	Describe
\.


--
-- Name: data_categories_category_id_seq; Type: SEQUENCE SET; Schema: public; Owner: transdb
--

SELECT pg_catalog.setval('data_categories_category_id_seq', 24, true);


--
-- Data for Name: data_items; Type: TABLE DATA; Schema: public; Owner: transdb
--

COPY data_items (item_id, name, description, category_id) FROM stdin;
51	dfgdfg	dfgdfgs sdfgsdfg	\N
48	asdf asdf asdf	a sdf asd fasdf	\N
49	xfbxcvbxcv dsfg sdfg	sd gsdf gsdfg	\N
50	asdfasdf	asdfasdf	\N
20	Web traffic logs	test	\N
21	Call logs	test	\N
22	Time and date of communications	test	\N
23	Other	test	\N
32	cell tower information	dump that	\N
33	cell tower information!	dump that	\N
34	That cell tower info, though	dump that	\N
35	That cell tower info, though	dump that	\N
36	That cell tower info, though	dump that	\N
37	That cell tower info, though	dump that	\N
38	That cell tower info, though	dump that	\N
39	That cell tower info, though	dump that	\N
40	test	test test	\N
41	test	test test	\N
42	asdfasdf	adfgsdfg sfdsfgd	\N
43	test test	test	\N
44	asdfasdf	asdfasdfasd	\N
45	Cell tower info	test	\N
47	dfhgdf	dfgdfg	\N
62	Other	test	19
59	Web traffic logs		19
60	Call logs		19
61	Time and date of communications		19
69	Messages between individual and organization		6
70	Messages between users		6
71	Content posted to service		6
72	Other		6
63	Geolocation		5
64	IP Address		5
65	Websites visited		5
66	Websites visited (external)		5
67	Search history		5
74	Billing Info		4
75	Email Address		4
76	Phone Number		4
77	Username		4
78	Other		4
73	Address		4
83	Date Joined Service	This indicates the date and time when a person signed up for an account with the service	4
84	New log type	here is the description	19
\.


--
-- Name: data_items_item_id_seq; Type: SEQUENCE SET; Schema: public; Owner: transdb
--

SELECT pg_catalog.setval('data_items_item_id_seq', 84, true);


--
-- Data for Name: data_retention_guide_categories; Type: TABLE DATA; Schema: public; Owner: transdb
--

COPY data_retention_guide_categories (guide_id, guide_data_category_id, inclusion_status, retention_status, guide_category_id) FROM stdin;
38	19	t	\N	143
38	6	t	\N	144
38	4	t	\N	146
\.


--
-- Name: data_retention_guide_categories_guide_category_id_seq; Type: SEQUENCE SET; Schema: public; Owner: transdb
--

SELECT pg_catalog.setval('data_retention_guide_categories_guide_category_id_seq', 152, true);


--
-- Data for Name: data_retention_guide_items; Type: TABLE DATA; Schema: public; Owner: transdb
--

COPY data_retention_guide_items (guide_id, guide_data_item_id, narrative, inclusion_status, retention_status, guide_item_id, guide_category_id, retention_period, retention_period_unit) FROM stdin;
38	60	\N	f	\N	691	143	\N	\N
38	62	\N	f	\N	693	143	\N	\N
38	69	\N	f	\N	694	144	\N	\N
38	72	\N	f	\N	697	144	\N	\N
38	78	\N	f	\N	709	146	\N	\N
38	59	\N	t	\N	690	143	1	2
38	61	\N	t	\N	692	143	2	1
38	70	\N	t	\N	695	144	6	4
38	71	\N	t	\N	696	144	10	1
38	73	\N	t	\N	704	146	1	1
38	74	\N	t	\N	705	146	1	1
38	75	\N	t	\N	706	146	\N	\N
38	76	\N	t	\N	707	146	1	1
38	77	\N	t	\N	708	146	\N	1
38	83	\N	t	\N	710	146	5	1
\.


--
-- Name: data_retention_guide_items_guide_item_id_seq; Type: SEQUENCE SET; Schema: public; Owner: transdb
--

SELECT pg_catalog.setval('data_retention_guide_items_guide_item_id_seq', 731, true);


--
-- Data for Name: data_retention_guides; Type: TABLE DATA; Schema: public; Owner: transdb
--

COPY data_retention_guides (guide_id, inclusion_status, complete_status, narrative, transparency_report_id, date_updated) FROM stdin;
1	t	f	test test test	\N	\N
2	t	f	This is a test. Yep.sd ""asda""	\N	\N
4	t	f	test	\N	\N
5	t	f	asfdasdf	\N	\N
8	t	f	test tes test	\N	\N
9	t	f	sadsd	\N	\N
7	t	f	asdfasdf sdafasdf	\N	\N
10	t	f	sdfgsdfgsdfg	\N	\N
11	t	f	fghdfghdfgh	\N	\N
12	\N	\N	fghfgh	\N	\N
22	\N	\N	\N	\N	\N
21	\N	\N	xfgfg sdf sdf gdsf gsdfg sdfg sdfg sdfg	\N	\N
20	\N	\N	\N	\N	\N
16	\N	\N	\N	\N	\N
19	\N	\N	asdf asdf asdf asdf	\N	\N
18	\N	\N	\N	\N	\N
17	\N	\N	\N	\N	\N
15	\N	\N	\N	\N	\N
14	\N	\N	\N	\N	\N
13	\N	\N	\N	\N	\N
23	\N	\N	\N	\N	\N
38	t	t	\N	76	2016-06-24
\.


--
-- Name: data_retention_guides_guide_id_seq; Type: SEQUENCE SET; Schema: public; Owner: transdb
--

SELECT pg_catalog.setval('data_retention_guides_guide_id_seq', 39, true);


--
-- Data for Name: government_request_categories; Type: TABLE DATA; Schema: public; Owner: transdb
--

COPY government_request_categories (category_id, name, description) FROM stdin;
1	General Disclosures	asdfasdf!!
2	Court Ordered (Warranted) Disclosures	Court ordered disclosures refer to production orders, summons, subpoenas, and search warrants that are issued by a judge or judicial officer. They compel a company to collect and disclose information under the organization's control. In some cases an organization may challenge the disclosure of the information prior to disclosing it to the requesting government agency. Organizations should consult with counsel to determine their legal options in responding to court ordered disclosures of information to government agencies.\n\nThere are many different types of court ordered (warranted) disclosures. Some of the most common types of disclosures are included here by default.
5	Other Disclosures	\N
\.


--
-- Name: government_request_categories_category_id_seq; Type: SEQUENCE SET; Schema: public; Owner: transdb
--

SELECT pg_catalog.setval('government_request_categories_category_id_seq', 5, true);


--
-- Data for Name: government_request_report_type_disclosures; Type: TABLE DATA; Schema: public; Owner: transdb
--

COPY government_request_report_type_disclosures (disclosure_id, request_report_id, request_type_id) FROM stdin;
243	27	12
244	27	13
245	27	8
246	27	7
247	27	9
248	27	10
249	27	11
250	27	3
251	27	5
252	27	6
253	27	4
254	27	1
\.


--
-- Name: government_request_report_type_disclosures_disclosure_id_seq; Type: SEQUENCE SET; Schema: public; Owner: transdb
--

SELECT pg_catalog.setval('government_request_report_type_disclosures_disclosure_id_seq', 266, true);


--
-- Data for Name: government_request_responses; Type: TABLE DATA; Schema: public; Owner: transdb
--

COPY government_request_responses (response_id, name, description) FROM stdin;
2	Number of requests	Counting the number of requests entails adding the voluntary or court-mandated requests or orders received by an organization, as appropriate for each of the types of reporting categories.
4	Number of requests rejected	Organizations may sometimes reject requests for information that are made by government agencies. Rejections might be on the basis of improper request formats, on the basis of refusing to provide information absent a court order, or on the basis of other process or legal grounds. When preparing their reports, organizations should tabulate all of the legal or voluntary requests that they refuse, instead of tabulating the number of subscribers who would otherwise be affected by the request.
5	Number of requests contested	Organizations may sometimes dispute the requests that they receive from government agencies as a result of improperly scoped legal requests, on the basis of erroneous legal authorities being used to compel data from an organization, or on the basis of doubts concerning the legality or constitutionality of the request. Organizations should count each request they oppose, as opposed to tabulating the number of subscribers/accounts/customers who are affected by the initial request and subsequent contestation.
6	Number of requests for which the organization has no data	Government agencies may sometimes make requests or demands for information where the organization does not possess any relevant information. Organizations should count each request for which they lack data, as opposed to tabulating the number of subscribers, or accounts, or customers who would be affected by the request but for whom the organization possesses no relevant data.
7	Number of requests for which partial information disclosed	Government agencies may sometimes make requests or demands for information where the organization possesses only some relevant information. Organizations should count each request for which they partially possess data, as opposed to tabulating the number of subscribers/accounts/customers who would be affected by the request but for whom the organization only partially possesses data.
8	Number of requests for which information is fully disclosed	Government agencies may sometimes make requests or demands for information where the organization fully discloses the requested or demanded information. Organizations should count each request for which they fully disclose data, as opposed to tabulating the number of subscribers/accounts/customers who are affected by the disclosure.
9	Number of users notified	Government agencies' requests will often affect a series of an organization's subscribers, customers, or users. Sometimes, though not always, organizations may notify those affected of the request. Organizations should count each affected person that they notify of the request; where they a barred from informing all those affected an organization might denote that with a footnote associated with the reported number.
3	Number of subscribers / accounts / customers affected	It is possible that a single request might affect multiple subscribers, or accounts, or customers. A single order might name or otherwise identify each of the subscribers, or accounts, or customers or include an 'identifier' -- a piece of data that is then used by the organization to subsequently identify the subscribers, or accounts, or customers associated with the request. When preparing their reports, organizations should tabulate all of the subscribers, or accounts, or customers affected by each of the types of reporting category requests.
\.


--
-- Name: government_request_responses_response_id_seq; Type: SEQUENCE SET; Schema: public; Owner: transdb
--

SELECT pg_catalog.setval('government_request_responses_response_id_seq', 9, true);


--
-- Data for Name: government_request_types; Type: TABLE DATA; Schema: public; Owner: transdb
--

COPY government_request_types (type_id, category_id, name, description) FROM stdin;
1	1	Voluntary Disclosure Following Government Request	Government agencies will sometimes ask organizations to voluntarily provide certain information to the requesting authority. In some cases these requests may be made where the agency does not believe a warrant or court order is required to obtain the information, such as when conducting criminal investigations, to location or notify next-of-kin, return property, or help search for missing persons. Organizations are permitted to ask the requesting agency to return with a court order or explain what statute requires the disclosure before volunteering the requested information.
3	1	Voluntary Disclosure at Organization's Initiative	Organizations may voluntarily share information with government agencies, though organizations may prefer to consult with counsel before doing so in order to ensure they are properly respecting any terms of service, contracts, or other guarantees made between the organization and its customers/subscribers/users, as well as acting in compliance with Canadian law. When voluntarily disclosing information the organization provides information without the receiving government agency in question first requesting the relevant information.
4	1	Disclosure in Emergency or Exigent Circumstances	Government agencies may sometimes request rapid or immediate access to information retained by organizations due to exigent circumstances, where the agencies would normally require a court order to access the information in question. Such requests may be for: identifying information (e.g. customer name, telephone number, mailing address, email address, or other information needed by the organization to identify its subscribers or customers) as well as communications content or transmission data.
5	1	Disclosures to Comply with Federal Law	Federal government agencies may sometimes compel organizations to disclose information by exercising statutory authorities; this means that the agencies do not require a court order to compel the information from an organization. Some organizations refer to these as 'government requirement letters'.
6	1	Disclosures to Comply with Provincial Law	Provincial government agencies may sometimes compel organizations to disclose information by exercising statutory authorities; this means that the agencies do not require a court order to compel the information from an organization. Some organizations refer to these as 'government requirement letters'.
7	2	Basic identifying information (court ordered)	Such orders compel an organization to collect and disclose personal identifiers associated with a subscribers/customer/user. Identifiers may include customer name, telephone number, mailing address, email address, or other identifiers needed to identify a person where those identifiers enjoy a reasonable expectation of privacy and can only be disclosed pursuant to a court order.
8	2	Tracking data	Tracking data orders are obtained using tracking warrants, as denoted under s.492.1 of the Criminal Code. These orders are used to obtain data that relates to the location of a transaction, individual, or thing.
9	2	Transmission data	Transmission data orders are obtained using a transmission data recorder order, as denoted under s.492.2 of the Criminal Code. These orders are used to obtain data that is obtained by dialling, addressing, routing, or signalling, such as incoming and outgoing times of calls, non-content information associated with text messages or chat-based communications, or other data that does not reveal the content of the communication or message. Transmission data is more commonly known as 'metadata'.
10	2	Stored communications and other stored data	Stored communications and other stored data is often obtained using a warrant and production orders, as denoted under s.487, 487.01, and 487.014-487.018 of the Criminal Code. These orders may refer to historical data that includes the content of stored communications including email, chat messages, photos, documents, or any other kinds of stored data.
11	2	Real time interceptions	Real time interceptions are often obtained using a wiretap warrant, as denoted under Part VI of the Criminal Code. These orders may refer to private communications which are intercepted by means of electro-magnetic, acoustic, mechanical, or other means and involve the live capture of communications that are intermediated or accessible by the organization.
12	5	Foreign Agency Requests (Court Ordered)	Canadian organizations may sometimes receive requests from non-Canadian agencies for access to information held by to Canadian organization. Such orders may be accompanied by a court order from the agency's jurisdiction. Alternately, the foreign order might be facilitated by Canadian agencies per the Mutual Legal Assistance in Criminal Matters Act.
13	5	Preservation Demands and Orders	Preservation demands and orders can be obtained under s.487.012 and 487.013 of the Criminal Code. Demands are made by peace or public officers whereas orders are made pursuant to judicial authority. These orders compel an organization to retain to identified information for 21 days (for domestic demands and orders) or 90 days (where the demand or order is made in order to assist an international investigation). Organizations are not required to disclose information prior to receiving a production order from the agency which served the demand or order. \nProduction orders are used to compel information from organizations, often after the organization has previously been compelled to preserve information after receiving a preservation demand or order. The preservation demands and orders category is used to identify the frequency at which preservation demands or orders are received, whereas the disclosure of actual data is reflected in one of the relevant court ordered disclosure category.
\.


--
-- Name: government_request_types_type_id_seq; Type: SEQUENCE SET; Schema: public; Owner: transdb
--

SELECT pg_catalog.setval('government_request_types_type_id_seq', 24, true);


--
-- Data for Name: government_requests_reports; Type: TABLE DATA; Schema: public; Owner: transdb
--

COPY government_requests_reports (report_id, transparency_report_id, inclusion_status, complete_status, narrative, date_updated) FROM stdin;
5	\N	\N	\N	\N	\N
13	\N	\N	\N	asdf asdf asdf asdf	\N
12	\N	\N	\N	\N	\N
10	\N	\N	\N	\N	\N
9	\N	\N	\N	\N	\N
11	\N	\N	\N	\N	\N
8	\N	\N	\N	\N	\N
7	\N	\N	\N	\N	\N
6	\N	\N	\N	\N	\N
27	76	t	t	About Our Organization\nOur organization provides chat- and message-based communication services to users and distributes our software through dominant mobile applications stores. We are committed to protecting our users' and subscribers' privacy while, at the same time, responsibly engaging with government agencies when they serve us with binding court orders or exercise powers under federal, provincial, or municipal law. \n\nAbout Our Services\nAs part of our offerings, our users and subscribers enjoy access to the following kinds of world-leading services:\n\n* secure instant messaging: we are unable to access the content of their communications. We rely on the [type] of encryption and private keys are generated and stored on end-point devices;\n* temporary accounts: we let users generate accounts that are not linked with mobile device identifiers, and these accounts can be set to expire after a short period of time. Such account information is only retained for 3 days after deletion;\n* Basic web browsing services: our subscribers can navigate to websites that are shared by other users. Our browser is based on Webkit and we do not retain logs of user or subscriber browsing habits for more than 60 days.\n\nRejected Requests\nWe routinely reject requests from government agencies on the grounds that they are over broad or request information which we believe require different kinds of legal orders. We work with government agencies to clarify the kinds of information they are seeking and our interpretation of the requisite orders needed to access such information. All such meetings occur in the presence, or on our behalves by, our counsel.\n\nNotification to Users\nWe actively seeks to notify users and subscribers when a government agency has requested information pertaining to their accounts or communications. We are not always able to  notify subscribers because of gag orders, and our total notification of users may not be fully reflective of all persons we will notify pursuant to government agency requests we have received over this reporting period. We wait at least 365 days before notifying subscribers and users in order for government agencies to either notify the individuals affected themselves, as well as to avoid disrupting investigations or other government activity. As such, the numbers of persons notified this year within each of the categories predominantly pertains to those affected by government access requests in the previous (Jan 1, 2014 - Dec 31 2014) reporting period.\n\nThis document and all materials associated with it are copyrighted 2016.	2016-06-24
\.


--
-- Name: government_requests_reports_report_id_seq; Type: SEQUENCE SET; Schema: public; Owner: transdb
--

SELECT pg_catalog.setval('government_requests_reports_report_id_seq', 28, true);


--
-- Name: law_enfocement_handbook_action_categor_handbook_category_id_seq; Type: SEQUENCE SET; Schema: public; Owner: transdb
--

SELECT pg_catalog.setval('law_enfocement_handbook_action_categor_handbook_category_id_seq', 421, true);


--
-- Data for Name: law_enfocement_handbook_action_categories; Type: TABLE DATA; Schema: public; Owner: transdb
--

COPY law_enfocement_handbook_action_categories (handbook_id, action_category_id, inclusion_status, handbook_category_id) FROM stdin;
51	10	t	405
51	8	t	406
51	7	t	407
51	6	t	408
51	5	t	409
51	4	t	410
51	3	t	411
51	2	t	412
\.


--
-- Data for Name: law_enfocement_handbook_actions; Type: TABLE DATA; Schema: public; Owner: transdb
--

COPY law_enfocement_handbook_actions (handbook_id, action_id, narrative, inclusion_status, handbook_category_id, handbook_action_id) FROM stdin;
51	25	\N	f	405	1103
51	19	\N	f	407	1108
51	21	\N	f	407	1110
51	17	\N	f	408	1113
51	18	\N	f	408	1114
51	29	\N	f	409	1116
51	31	\N	f	409	1117
51	14	\N	f	410	1122
51	6	\N	f	411	1124
51	7	\N	t	411	1125
51	8	\N	t	411	1126
51	9	\N	t	411	1127
51	1	\N	f	412	1128
51	4	\N	f	412	1131
51	5	\N	f	412	1132
51	26	While our organization generally does not seek reimbursement for domestic cases, barring those which are unduly onerous on our organization and where Canadian law authorizes such reimbursement, we will always seek reimbursement for foreign cases where we are voluntarily choosing to provide data to foreign government agencies.	t	405	1104
51	27	\N	t	405	1105
51	23	Type of Service\nOur organization is committed to providing [description of service]. As part of our offerings, our users and subscribers enjoy access to the following kinds of world-leading services:\n\n* secure instant messaging: we are unable to access the content of their communications. We rely on the [type] of encryption and private keys are generated and stored on end-point devices;\n* temporary accounts: we let users generate accounts that are not linked with mobile device identifiers, and these accounts can be set to expire after a short period of time. Such account information is only retained for 3 days after deletion;\n* Basic web browsing services: our subscribers can navigate to websites that are shared by other users. Our browser is based on Webkit and we do not retain logs of user or subscriber browsing habits for more than 60 days.	t	406	1107
51	20	Emergency requests should be directed to (+x) xxx-xxxx. Government officials are expected to identify themselves, provide badge or government ID, name of supervisor, and an official email address so that we can confirm the authenticity of the requesting official.	t	407	1109
51	22	Emergency requests can be directed to example@example.com. Government officials are expected to identify themselves, provide badge or government ID, name of supervisor, use an official email address, and provide a phone number so that we can confirm the authenticity of the requesting official. Please note that example@example.com is monitored but may not be read for up to 24-48 hours.	t	407	1111
51	16	Our agency fully complies with lawful requests that are issued by countries in North America, Europe, Australia, and some parts of Asia. Please contact example@example.com to learn whether we will accept requests from your country.\n\nAll requests must be sent in either French or English. you should cite your domestic law (which must have an official English or French version or translation), provide a judicially authorized order authorizing your access to the requested data, and cite the equivalent Canadian law to your domestic legislation. \n\nIf you need assistance in finding which Canadian law correlates with your domestic law we suggest that you contact a relevant Canadian government agency.	t	408	1112
51	28	We commit to informing our users within 365 days of any government requests for their information, barring situations where we are prevented from so informing them due to a gag order.	t	409	1115
51	10	\N	t	410	1118
51	11	\N	t	410	1119
51	12	\N	t	410	1120
51	13	\N	t	410	1121
51	15	If your order requires immediate attention please indicate as such in your communications with us. While we cannot guarantee a faster response than indicated either through the relevant statutory law or judicial order, we will attempt to prioritize your requests as our resources permit.	t	410	1123
51	2	We will accept emergency, or exigent, requests through phone messages.	t	412	1129
51	3	For all non-exigent or emergency requests, we ask that you direct requests and orders to example@example.com.	t	412	1130
\.


--
-- Name: law_enfocement_handbook_actions_handbook_action_id_seq; Type: SEQUENCE SET; Schema: public; Owner: transdb
--

SELECT pg_catalog.setval('law_enfocement_handbook_actions_handbook_action_id_seq', 1162, true);


--
-- Data for Name: law_enforcement_action_categories; Type: TABLE DATA; Schema: public; Owner: transdb
--

COPY law_enforcement_action_categories (category_id, name, action_selection_type, description) FROM stdin;
5	User notification	1	This indicates whether an organization will notify persons who are affected by government agencies making requests for information pertaining to those persons.
10	Cost reimbursement	1	This indicates whether an organization will seek compensation for responding to government agencies' requests
8	Description of our services	3	This is a narrative box wherein organizations can explain the kinds of services that they provide to customers and subscribers
7	Policy on emergency requests	2	Organizations can identify how they will receive emergency requests from government agencies. Narrative that accompanies each option could include: specific contact information; time to respond to a request using the relevant mode of communication; and the time it will take an organization to respond.
6	How we respond to international requests	1	Organizations have the option to respond to international requests if they are a purely-Canadian organization. Select the option that indicates how your organization responds to international requests.
4	Required contact information	2	Organizations should note what information requesting government officials are expected to include with their requests.
3	Types of organizational disclosures	2	While organizations must be responsive to binding orders they may decide whether they will also sometimes voluntarily disclose information when not otherwise obliged to.
2	How should requests be sent to our organization?	2	Organizations should indicate what methods they would like to receive requests. We suggest that relevant contact information be added for each mode of communication your organization is responsive to in the narrative window associated with each choice.
\.


--
-- Name: law_enforcement_action_categories_category_id_seq; Type: SEQUENCE SET; Schema: public; Owner: transdb
--

SELECT pg_catalog.setval('law_enforcement_action_categories_category_id_seq', 22, true);


--
-- Data for Name: law_enforcement_actions; Type: TABLE DATA; Schema: public; Owner: transdb
--

COPY law_enforcement_actions (action_id, category_id, name, narrative, narrative_label, inclusion_status_default) FROM stdin;
2	2	Phone	asdf	\N	\N
3	2	Email	test	\N	\N
4	2	Certified Mail	test	\N	\N
5	2	Courier	asdf	asdf	\N
11	4	Requesting Agency Officer Name / badge ID	asdfasd	\N	\N
12	4	Requesting Agent's email address	asdfasdf	\N	\N
13	4	Requesting Agent's Phone Contact	asdfasdf	\N	\N
14	4	Requesting Agency's Mailing Address	asdfasd	\N	\N
15	4	Requested Response Date	asdfasd	\N	\N
10	4	Requesting Agency Name	test	\N	\N
16	6	Accept	asdf	\N	\N
17	6	Reject	asdf	\N	\N
18	6	Require MLAT	asdf	\N	\N
19	7	Require Emergency Contact Letter	asdfasdf	\N	\N
20	7	Phone	asdf	\N	\N
21	7	Fax	adfgadfg	\N	\N
22	7	Email	asdf	\N	\N
23	8	Service provided	asdf	\N	\N
25	10	Will seek	asdf	\N	\N
26	10	Will sometimes seek	asdf	\N	\N
27	10	Will not seek	asdfasdf	\N	\N
28	5	Yes	asdf	\N	\N
29	5	No	asdf	\N	\N
31	5	Sometimes	asdf	\N	\N
1	2	Fax	Blah	\N	\N
7	3	Government statutory / requirement letters		\N	t
8	3	Court orders		\N	t
9	3	Emergency requests		\N	t
6	3	Non-Obligatory Requests		\N	\N
\.


--
-- Name: law_enforcement_actions_action_id_seq; Type: SEQUENCE SET; Schema: public; Owner: transdb
--

SELECT pg_catalog.setval('law_enforcement_actions_action_id_seq', 53, true);


--
-- Data for Name: law_enforcement_handbooks; Type: TABLE DATA; Schema: public; Owner: transdb
--

COPY law_enforcement_handbooks (handbook_id, inclusion_status, complete_status, narrative, date_updated, date_updated_inclusion_status, transparency_report_id) FROM stdin;
4	t	f	dfgdsgsdfg	\N	\N	\N
5	t	f	dfgdsgsdfg	\N	\N	\N
6	t	f	dfgdsgsdfg	\N	\N	\N
8	t	f	asdfasdf	\N	\N	\N
10	t	f	asDasd	\N	\N	\N
7	t	f	dfgdsgsdfg	\N	\N	\N
11	t	f	asdfasdf	\N	\N	\N
12	t	f	asdfasdf	\N	\N	\N
13	t	f	dsrsfgh	\N	\N	\N
14	\N	\N	\N	\N	\N	\N
25	\N	\N	\N	\N	\N	\N
24	\N	\N	These are our guidlines.	\N	\N	\N
23	\N	\N	asdf asd fasdf asdf asdf	\N	\N	\N
22	\N	\N	\N	\N	\N	\N
21	\N	\N	sdfg	\N	\N	\N
19	\N	\N	\N	\N	\N	\N
20	\N	\N	\N	\N	\N	\N
18	\N	\N	\N	\N	\N	\N
17	\N	\N	\N	\N	\N	\N
16	\N	\N	\N	\N	\N	\N
15	\N	\N	\N	\N	\N	\N
51	t	t	At [organization] we are committed to assisting authorities conduct their lawful investigations. Our government access handbook discusses the methods and processes that we have currently adopted to assist such agencies understand our policies pertaining to access to communications.\n\nWe are a small organization and, as such, may be challenged if we receive numerous or broad-based requests. Government agencies should identify the specific accounts that they want us to collect data about; this can involve providing subscriber-related information (e.g. username, mobile phone number, email address) or information about the group chat (e.g. name of the chat group and date created, subscriber information pertaining to at least two of the users or subscribers). \n\nWhile we commit to working with government agencies we are unable to allocate developer resources to creating tools or mechanisms for 'self-checkout' services that might let agencies export information directly from our systems. \n\nIf you have any questions concerning our policies we suggest that you contact example@example.com. That email address is monitored and we will respond to you within 3-5 business days.\n\nThis handbook is copyrighted as of 2016.	2016-06-24	\N	76
\.


--
-- Name: law_enforcement_handbooks_handbook_id_seq; Type: SEQUENCE SET; Schema: public; Owner: transdb
--

SELECT pg_catalog.setval('law_enforcement_handbooks_handbook_id_seq', 52, true);


--
-- Data for Name: transparency_reports; Type: TABLE DATA; Schema: public; Owner: transdb
--

COPY transparency_reports (report_id, publication_status, complete_status, publication_date, report_period_start, report_period_end, author_name, date_updated) FROM stdin;
76	\N	t	2016-01-15	2015-01-01	2015-12-31	Christopher Parsons	2016-06-24
\.


--
-- Name: transparency_reports_report_id_seq; Type: SEQUENCE SET; Schema: public; Owner: transdb
--

SELECT pg_catalog.setval('transparency_reports_report_id_seq', 77, true);


--
-- Data for Name: type_disclosure_responses; Type: TABLE DATA; Schema: public; Owner: transdb
--

COPY type_disclosure_responses (response_id, disclosure_id, count, type_disclosure_id) FROM stdin;
7	243	0	1923
6	243	0	1924
5	243	0	1925
9	244	0	1929
8	244	0	1930
7	244	0	1931
6	244	0	1932
5	244	0	1933
4	244	0	1934
3	244	0	1935
2	244	0	1936
9	245	0	1937
8	245	0	1938
7	245	0	1939
6	245	0	1940
5	245	0	1941
4	245	0	1942
3	245	0	1943
2	245	0	1944
9	246	0	1945
8	246	0	1946
7	246	0	1947
6	246	0	1948
5	246	0	1949
4	246	0	1950
3	246	0	1951
2	246	0	1952
7	247	0	1955
6	247	0	1956
5	247	0	1957
4	247	0	1958
3	247	0	1959
9	248	0	1961
8	248	0	1962
6	248	0	1964
5	248	0	1965
4	248	0	1966
9	249	0	1969
8	249	0	1970
7	249	0	1971
6	249	0	1972
5	249	0	1973
4	249	0	1974
3	249	0	1975
2	249	0	1976
9	250	0	1977
8	250	0	1978
7	250	0	1979
6	250	0	1980
5	250	0	1981
4	250	0	1982
3	250	0	1983
2	250	0	1984
7	251	0	1987
5	251	0	1989
4	251	0	1990
7	252	0	1995
5	252	0	1997
9	253	0	2001
8	253	0	2002
7	253	0	2003
6	253	0	2004
5	253	0	2005
9	254	0	2009
8	254	0	2010
7	254	0	2011
6	254	0	2012
5	254	0	2013
4	254	0	2014
3	254	0	2015
2	254	0	2016
2	251	2	1992
3	251	13	1991
6	251	1	1988
8	251	1	1986
9	251	4	1985
2	252	16	2000
3	252	163	1999
4	252	5	1998
6	252	5	1996
8	252	6	1994
9	252	56	1993
2	253	1	2008
3	253	1	2007
4	253	1	2006
2	247	3	1960
8	247	3	1954
9	247	11	1953
2	248	1	1968
3	248	4	1967
7	248	1	1963
2	243	7	1928
3	243	55	1927
4	243	5	1926
8	243	2	1922
9	243	10	1921
\.


--
-- Name: type_disclosure_responses_type_disclosure_id_seq; Type: SEQUENCE SET; Schema: public; Owner: transdb
--

SELECT pg_catalog.setval('type_disclosure_responses_type_disclosure_id_seq', 2112, true);


--
-- Name: data_categories_pkey; Type: CONSTRAINT; Schema: public; Owner: transdb; Tablespace: 
--

ALTER TABLE ONLY data_categories
    ADD CONSTRAINT data_categories_pkey PRIMARY KEY (category_id);


--
-- Name: data_items_pkey; Type: CONSTRAINT; Schema: public; Owner: transdb; Tablespace: 
--

ALTER TABLE ONLY data_items
    ADD CONSTRAINT data_items_pkey PRIMARY KEY (item_id);


--
-- Name: data_retention_guide_categories_pkey; Type: CONSTRAINT; Schema: public; Owner: transdb; Tablespace: 
--

ALTER TABLE ONLY data_retention_guide_categories
    ADD CONSTRAINT data_retention_guide_categories_pkey PRIMARY KEY (guide_category_id);


--
-- Name: data_retention_guide_items_pkey; Type: CONSTRAINT; Schema: public; Owner: transdb; Tablespace: 
--

ALTER TABLE ONLY data_retention_guide_items
    ADD CONSTRAINT data_retention_guide_items_pkey PRIMARY KEY (guide_item_id);


--
-- Name: data_retention_guides_pkey; Type: CONSTRAINT; Schema: public; Owner: transdb; Tablespace: 
--

ALTER TABLE ONLY data_retention_guides
    ADD CONSTRAINT data_retention_guides_pkey PRIMARY KEY (guide_id);


--
-- Name: government_request_categories_pkey; Type: CONSTRAINT; Schema: public; Owner: transdb; Tablespace: 
--

ALTER TABLE ONLY government_request_categories
    ADD CONSTRAINT government_request_categories_pkey PRIMARY KEY (category_id);


--
-- Name: government_request_report_type_disclosures_pkey; Type: CONSTRAINT; Schema: public; Owner: transdb; Tablespace: 
--

ALTER TABLE ONLY government_request_report_type_disclosures
    ADD CONSTRAINT government_request_report_type_disclosures_pkey PRIMARY KEY (disclosure_id);


--
-- Name: government_request_responses_pkey; Type: CONSTRAINT; Schema: public; Owner: transdb; Tablespace: 
--

ALTER TABLE ONLY government_request_responses
    ADD CONSTRAINT government_request_responses_pkey PRIMARY KEY (response_id);


--
-- Name: government_request_types_pkey; Type: CONSTRAINT; Schema: public; Owner: transdb; Tablespace: 
--

ALTER TABLE ONLY government_request_types
    ADD CONSTRAINT government_request_types_pkey PRIMARY KEY (type_id);


--
-- Name: government_requests_reports_pkey; Type: CONSTRAINT; Schema: public; Owner: transdb; Tablespace: 
--

ALTER TABLE ONLY government_requests_reports
    ADD CONSTRAINT government_requests_reports_pkey PRIMARY KEY (report_id);


--
-- Name: law_enfocement_handbook_action_categories_pkey; Type: CONSTRAINT; Schema: public; Owner: transdb; Tablespace: 
--

ALTER TABLE ONLY law_enfocement_handbook_action_categories
    ADD CONSTRAINT law_enfocement_handbook_action_categories_pkey PRIMARY KEY (handbook_category_id);


--
-- Name: law_enfocement_handbook_actions_pkey; Type: CONSTRAINT; Schema: public; Owner: transdb; Tablespace: 
--

ALTER TABLE ONLY law_enfocement_handbook_actions
    ADD CONSTRAINT law_enfocement_handbook_actions_pkey PRIMARY KEY (handbook_action_id);


--
-- Name: law_enforcement_action_categories_pkey; Type: CONSTRAINT; Schema: public; Owner: transdb; Tablespace: 
--

ALTER TABLE ONLY law_enforcement_action_categories
    ADD CONSTRAINT law_enforcement_action_categories_pkey PRIMARY KEY (category_id);


--
-- Name: law_enforcement_actions_pkey; Type: CONSTRAINT; Schema: public; Owner: transdb; Tablespace: 
--

ALTER TABLE ONLY law_enforcement_actions
    ADD CONSTRAINT law_enforcement_actions_pkey PRIMARY KEY (action_id);


--
-- Name: law_enforcement_handbooks_pkey; Type: CONSTRAINT; Schema: public; Owner: transdb; Tablespace: 
--

ALTER TABLE ONLY law_enforcement_handbooks
    ADD CONSTRAINT law_enforcement_handbooks_pkey PRIMARY KEY (handbook_id);


--
-- Name: transparency_reports_pkey; Type: CONSTRAINT; Schema: public; Owner: transdb; Tablespace: 
--

ALTER TABLE ONLY transparency_reports
    ADD CONSTRAINT transparency_reports_pkey PRIMARY KEY (report_id);


--
-- Name: type_disclosure_responses_pkey; Type: CONSTRAINT; Schema: public; Owner: transdb; Tablespace: 
--

ALTER TABLE ONLY type_disclosure_responses
    ADD CONSTRAINT type_disclosure_responses_pkey PRIMARY KEY (type_disclosure_id);


--
-- Name: data_items_category_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: transdb
--

ALTER TABLE ONLY data_items
    ADD CONSTRAINT data_items_category_id_fkey FOREIGN KEY (category_id) REFERENCES data_categories(category_id) ON DELETE CASCADE;


--
-- Name: data_retention_guide_categories_guide_data_category_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: transdb
--

ALTER TABLE ONLY data_retention_guide_categories
    ADD CONSTRAINT data_retention_guide_categories_guide_data_category_id_fkey FOREIGN KEY (guide_data_category_id) REFERENCES data_categories(category_id) ON DELETE CASCADE;


--
-- Name: data_retention_guide_categories_guide_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: transdb
--

ALTER TABLE ONLY data_retention_guide_categories
    ADD CONSTRAINT data_retention_guide_categories_guide_id_fkey FOREIGN KEY (guide_id) REFERENCES data_retention_guides(guide_id) ON DELETE CASCADE;


--
-- Name: data_retention_guide_items_guide_category_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: transdb
--

ALTER TABLE ONLY data_retention_guide_items
    ADD CONSTRAINT data_retention_guide_items_guide_category_id_fkey FOREIGN KEY (guide_category_id) REFERENCES data_retention_guide_categories(guide_category_id) ON DELETE CASCADE;


--
-- Name: data_retention_guide_items_guide_data_item_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: transdb
--

ALTER TABLE ONLY data_retention_guide_items
    ADD CONSTRAINT data_retention_guide_items_guide_data_item_id_fkey FOREIGN KEY (guide_data_item_id) REFERENCES data_items(item_id) ON DELETE CASCADE;


--
-- Name: data_retention_guide_items_guide_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: transdb
--

ALTER TABLE ONLY data_retention_guide_items
    ADD CONSTRAINT data_retention_guide_items_guide_id_fkey FOREIGN KEY (guide_id) REFERENCES data_retention_guides(guide_id) ON DELETE CASCADE;


--
-- Name: data_retention_guides_transparency_report_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: transdb
--

ALTER TABLE ONLY data_retention_guides
    ADD CONSTRAINT data_retention_guides_transparency_report_id_fkey FOREIGN KEY (transparency_report_id) REFERENCES transparency_reports(report_id) ON DELETE CASCADE;


--
-- Name: government_request_report_type_disclosur_request_report_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: transdb
--

ALTER TABLE ONLY government_request_report_type_disclosures
    ADD CONSTRAINT government_request_report_type_disclosur_request_report_id_fkey FOREIGN KEY (request_report_id) REFERENCES government_requests_reports(report_id) ON DELETE CASCADE;


--
-- Name: government_request_report_type_disclosures_request_type_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: transdb
--

ALTER TABLE ONLY government_request_report_type_disclosures
    ADD CONSTRAINT government_request_report_type_disclosures_request_type_id_fkey FOREIGN KEY (request_type_id) REFERENCES government_request_types(type_id) ON DELETE CASCADE;


--
-- Name: government_request_types_category_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: transdb
--

ALTER TABLE ONLY government_request_types
    ADD CONSTRAINT government_request_types_category_id_fkey FOREIGN KEY (category_id) REFERENCES government_request_categories(category_id) ON DELETE CASCADE;


--
-- Name: government_requests_reports_transparency_report_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: transdb
--

ALTER TABLE ONLY government_requests_reports
    ADD CONSTRAINT government_requests_reports_transparency_report_id_fkey FOREIGN KEY (transparency_report_id) REFERENCES transparency_reports(report_id) ON DELETE CASCADE;


--
-- Name: law_enfocement_handbook_action_categori_action_category_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: transdb
--

ALTER TABLE ONLY law_enfocement_handbook_action_categories
    ADD CONSTRAINT law_enfocement_handbook_action_categori_action_category_id_fkey FOREIGN KEY (action_category_id) REFERENCES law_enforcement_action_categories(category_id) ON DELETE CASCADE;


--
-- Name: law_enfocement_handbook_action_categories_handbook_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: transdb
--

ALTER TABLE ONLY law_enfocement_handbook_action_categories
    ADD CONSTRAINT law_enfocement_handbook_action_categories_handbook_id_fkey FOREIGN KEY (handbook_id) REFERENCES law_enforcement_handbooks(handbook_id) ON DELETE CASCADE;


--
-- Name: law_enfocement_handbook_actions_action_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: transdb
--

ALTER TABLE ONLY law_enfocement_handbook_actions
    ADD CONSTRAINT law_enfocement_handbook_actions_action_id_fkey FOREIGN KEY (action_id) REFERENCES law_enforcement_actions(action_id) ON DELETE CASCADE;


--
-- Name: law_enfocement_handbook_actions_handbook_category_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: transdb
--

ALTER TABLE ONLY law_enfocement_handbook_actions
    ADD CONSTRAINT law_enfocement_handbook_actions_handbook_category_id_fkey FOREIGN KEY (handbook_category_id) REFERENCES law_enfocement_handbook_action_categories(handbook_category_id) ON DELETE CASCADE;


--
-- Name: law_enfocement_handbook_actions_handbook_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: transdb
--

ALTER TABLE ONLY law_enfocement_handbook_actions
    ADD CONSTRAINT law_enfocement_handbook_actions_handbook_id_fkey FOREIGN KEY (handbook_id) REFERENCES law_enforcement_handbooks(handbook_id) ON DELETE CASCADE;


--
-- Name: law_enforcement_actions_category_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: transdb
--

ALTER TABLE ONLY law_enforcement_actions
    ADD CONSTRAINT law_enforcement_actions_category_id_fkey FOREIGN KEY (category_id) REFERENCES law_enforcement_action_categories(category_id) ON DELETE CASCADE;


--
-- Name: law_enforcement_handbooks_transparency_report_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: transdb
--

ALTER TABLE ONLY law_enforcement_handbooks
    ADD CONSTRAINT law_enforcement_handbooks_transparency_report_id_fkey FOREIGN KEY (transparency_report_id) REFERENCES transparency_reports(report_id) ON DELETE CASCADE;


--
-- Name: type_disclosure_responses_disclosure_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: transdb
--

ALTER TABLE ONLY type_disclosure_responses
    ADD CONSTRAINT type_disclosure_responses_disclosure_id_fkey FOREIGN KEY (disclosure_id) REFERENCES government_request_report_type_disclosures(disclosure_id) ON DELETE CASCADE;


--
-- Name: type_disclosure_responses_response_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: transdb
--

ALTER TABLE ONLY type_disclosure_responses
    ADD CONSTRAINT type_disclosure_responses_response_id_fkey FOREIGN KEY (response_id) REFERENCES government_request_responses(response_id) ON DELETE CASCADE;


--
-- Name: public; Type: ACL; Schema: -; Owner: postgres
--

REVOKE ALL ON SCHEMA public FROM PUBLIC;
REVOKE ALL ON SCHEMA public FROM postgres;
GRANT ALL ON SCHEMA public TO postgres;
GRANT ALL ON SCHEMA public TO PUBLIC;


--
-- PostgreSQL database dump complete
--

