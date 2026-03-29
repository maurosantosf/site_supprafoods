-- ==========================================================================================
-- Script: create_dw_suppra_foods.sql
-- Propósito: Criar o banco de dados DW_SUPPRA_FOODS e configurar estrutura de acesso
-- ==========================================================================================

USE master;
GO

-- 1. Criar o Banco de Dados
IF NOT EXISTS (SELECT name FROM sys.databases WHERE name = N'DW_SUPPRA_FOODS')
BEGIN
    PRINT 'Criando banco de dados DW_SUPPRA_FOODS...'
    CREATE DATABASE [DW_SUPPRA_FOODS];
END
ELSE
BEGIN
    PRINT 'O banco de dados DW_SUPPRA_FOODS já existe.'
END
GO

USE [DW_SUPPRA_FOODS];
GO

-- 2. Configurações de Acesso (Exemplo para Gateway/Power BI)
-- Descomente e altere a senha caso deseje criar um usuário específico para leitura
/*
IF NOT EXISTS (SELECT * FROM sys.server_principals WHERE name = N'usr_powerbi')
BEGIN
    CREATE LOGIN [usr_powerbi] WITH PASSWORD = 'SuaSenhaForteAqui123!', DEFAULT_DATABASE=[DW_SUPPRA_FOODS], CHECK_EXPIRATION=OFF, CHECK_POLICY=OFF;
END
GO

IF NOT EXISTS (SELECT * FROM sys.database_principals WHERE name = N'usr_powerbi')
BEGIN
    CREATE USER [usr_powerbi] FOR LOGIN [usr_powerbi];
    EXEC sp_addrolemember 'db_datareader', 'usr_powerbi';
END
GO
*/

PRINT 'Configuração inicial concluída.'
GO
