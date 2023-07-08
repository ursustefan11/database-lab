IF NOT EXISTS(SELECT 1 FROM sys.server_principals WHERE name = N'python_insert')
BEGIN

    CREATE LOGIN python_insert
    WITH PASSWORD = 'SECURITY',
        DEFAULT_DATABASE = NewSample,
        CHECK_POLICY = OFF

END;
GO

USE NewSample
GO

IF NOT EXISTS(SELECT 1 FROM sys.database_principals WHERE name = N'python_user')
BEGIN

    CREATE USER python_user FOR LOGIN python_insert
END;
GO


CREATE ROLE Script

GRANT SELECT, INSERT ON Schema::Application TO Script
GRANT SELECT, INSERT ON Schema::Sales TO Script
GRANT SELECT, INSERT ON Schema::Inventory TO Script
GRANT SELECT, INSERT ON Schema::HR TO Script
GRANT SELECT, INSERT ON Schema::Financial TO Script
GO

EXEC sp_addrolemember N'Script', N'python_user'

/*
DROP LOGIN python_insert
DROP USER python_user
DROP ROLE Script
*/
