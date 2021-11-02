create database sad_test;
use sad_test;

CREATE TABLE DIM_TEMPO (
	Id_Tempo int IDENTITY(1,1) NOT NULL,
	Data datetime NOT NULL,
	Dia smallint NOT NULL,
	DiaSemana varchar(25) NOT NULL,
	FimSemana char(3) NOT NULL,
	Quinzena smallint NOT NULL,
	Mes smallint NOT NULL,
	NomeMes varchar(20) NOT NULL,
	FimMes char(3) NOT NULL,
	Trimestre smallint NOT NULL,
	NomeTrimestre varchar(20) NOT NULL,
	Semestre smallint NOT NULL,
	NomeSemestre varchar(20) NOT NULL,
	Ano smallint NOT NULL,
	PRIMARY KEY (Id_Tempo)
)

