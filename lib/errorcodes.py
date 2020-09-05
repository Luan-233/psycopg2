"""Error codes for PostgresSQL

This module contains symbolic names for all PostgreSQL error codes.
"""
# psycopg2/errorcodes.py - PostgreSQL error codes
#
# Copyright (C) 2006-2019 Johan Dahlin  <jdahlin@async.com.br>
# Copyright (C) 2020 The Psycopg Team
#
# psycopg2 is free software: you can redistribute it and/or modify it
# under the terms of the GNU Lesser General Public License as published
# by the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# In addition, as a special exception, the copyright holders give
# permission to link this program with the OpenSSL library (or with
# modified versions of OpenSSL that use the same license as OpenSSL),
# and distribute linked combinations including the two.
#
# You must obey the GNU Lesser General Public License in all respects for
# all of the code used other than OpenSSL.
#
# psycopg2 is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
# FITNESS FOR A PARTICULAR PURPOSE.  See the GNU Lesser General Public
# License for more details.
#
# Based on:
#
#   https://www.postgresql.org/docs/current/static/errcodes-appendix.html
#


def lookup(code, _cache={}):
    """Lookup an error code or class code and return its symbolic name.

    Raise `KeyError` if the code is not found.
    """
    if _cache:
        return _cache[code]

    # Generate the lookup map at first usage.
    tmp = {}
    for k, v in globals().items():
        if isinstance(v, str) and len(v) in (2, 5):
            # Strip trailing underscore used to disambiguate duplicate values
            tmp[v] = k.rstrip("_")

    assert tmp

    # Atomic update, to avoid race condition on import (bug #382)
    _cache.update(tmp)

    return _cache[code]


# autogenerated data: do not edit below this point.

# Error classes
CLASS_SUCCESSFUL_COMPLETION = '00'
CLASS_WARNING = '01'
CLASS_NO_DATA = '02'
CLASS_SQL_STATEMENT_NOT_YET_COMPLETE = '03'
CLASS_CONNECTION_EXCEPTION = '08'
CLASS_TRIGGERED_ACTION_EXCEPTION = '09'
CLASS_FEATURE_NOT_SUPPORTED = '0A'
CLASS_INVALID_TRANSACTION_INITIATION = '0B'
CLASS_LOCATOR_EXCEPTION = '0F'
CLASS_INVALID_GRANTOR = '0L'
CLASS_INVALID_ROLE_SPECIFICATION = '0P'
CLASS_DIAGNOSTICS_EXCEPTION = '0Z'
CLASS_CASE_NOT_FOUND = '20'
CLASS_CARDINALITY_VIOLATION = '21'
CLASS_DATA_EXCEPTION = '22'
CLASS_INTEGRITY_CONSTRAINT_VIOLATION = '23'
CLASS_INVALID_CURSOR_STATE = '24'
CLASS_INVALID_TRANSACTION_STATE = '25'
CLASS_INVALID_SQL_STATEMENT_NAME = '26'
CLASS_TRIGGERED_DATA_CHANGE_VIOLATION = '27'
CLASS_INVALID_AUTHORIZATION_SPECIFICATION = '28'
CLASS_DEPENDENT_PRIVILEGE_DESCRIPTORS_STILL_EXIST = '2B'
CLASS_INVALID_TRANSACTION_TERMINATION = '2D'
CLASS_SQL_ROUTINE_EXCEPTION = '2F'
CLASS_INVALID_CURSOR_NAME = '34'
CLASS_EXTERNAL_ROUTINE_EXCEPTION = '38'
CLASS_EXTERNAL_ROUTINE_INVOCATION_EXCEPTION = '39'
CLASS_SAVEPOINT_EXCEPTION = '3B'
CLASS_INVALID_CATALOG_NAME = '3D'
CLASS_INVALID_SCHEMA_NAME = '3F'
CLASS_TRANSACTION_ROLLBACK = '40'
CLASS_SYNTAX_ERROR_OR_ACCESS_RULE_VIOLATION = '42'
CLASS_WITH_CHECK_OPTION_VIOLATION = '44'
CLASS_INSUFFICIENT_RESOURCES = '53'
CLASS_PROGRAM_LIMIT_EXCEEDED = '54'
CLASS_OBJECT_NOT_IN_PREREQUISITE_STATE = '55'
CLASS_OPERATOR_INTERVENTION = '57'
CLASS_SYSTEM_ERROR = '58'
CLASS_SNAPSHOT_FAILURE = '72'
CLASS_CONFIGURATION_FILE_ERROR = 'F0'
CLASS_FOREIGN_DATA_WRAPPER_ERROR = 'HV'
CLASS_PL_PGSQL_ERROR = 'P0'
CLASS_INTERNAL_ERROR = 'XX'

# Class 00 - Successful Completion
SUCCESSFUL_COMPLETION = '00000'

# Class 01 - Warning
WARNING = '01000'
NULL_VALUE_ELIMINATED_IN_SET_FUNCTION = '01003'
STRING_DATA_RIGHT_TRUNCATION_ = '01004'
PRIVILEGE_NOT_REVOKED = '01006'
PRIVILEGE_NOT_GRANTED = '01007'
IMPLICIT_ZERO_BIT_PADDING = '01008'
DYNAMIC_RESULT_SETS_RETURNED = '0100C'
DEPRECATED_FEATURE = '01P01'

# Class 02 - No Data (this is also a warning class per the SQL standard)
NO_DATA = '02000'
NO_ADDITIONAL_DYNAMIC_RESULT_SETS_RETURNED = '02001'

# Class 03 - SQL Statement Not Yet Complete
SQL_STATEMENT_NOT_YET_COMPLETE = '03000'

# Class 08 - Connection Exception
CONNECTION_EXCEPTION = '08000'
SQLCLIENT_UNABLE_TO_ESTABLISH_SQLCONNECTION = '08001'
CONNECTION_DOES_NOT_EXIST = '08003'
SQLSERVER_REJECTED_ESTABLISHMENT_OF_SQLCONNECTION = '08004'
CONNECTION_FAILURE = '08006'
TRANSACTION_RESOLUTION_UNKNOWN = '08007'
PROTOCOL_VIOLATION = '08P01'

# Class 09 - Triggered Action Exception
TRIGGERED_ACTION_EXCEPTION = '09000'

# Class 0A - Feature Not Supported
FEATURE_NOT_SUPPORTED = '0A000'

# Class 0B - Invalid Transaction Initiation
INVALID_TRANSACTION_INITIATION = '0B000'

# Class 0F - Locator Exception
LOCATOR_EXCEPTION = '0F000'
INVALID_LOCATOR_SPECIFICATION = '0F001'

# Class 0L - Invalid Grantor
INVALID_GRANTOR = '0L000'
INVALID_GRANT_OPERATION = '0LP01'

# Class 0P - Invalid Role Specification
INVALID_ROLE_SPECIFICATION = '0P000'

# Class 0Z - Diagnostics Exception
DIAGNOSTICS_EXCEPTION = '0Z000'
STACKED_DIAGNOSTICS_ACCESSED_WITHOUT_ACTIVE_HANDLER = '0Z002'

# Class 20 - Case Not Found
CASE_NOT_FOUND = '20000'

# Class 21 - Cardinality Violation
CARDINALITY_VIOLATION = '21000'

# Class 22 - Data Exception
DATA_EXCEPTION = '22000'
STRING_DATA_RIGHT_TRUNCATION = '22001'
NULL_VALUE_NO_INDICATOR_PARAMETER = '22002'
NUMERIC_VALUE_OUT_OF_RANGE = '22003'
NULL_VALUE_NOT_ALLOWED_ = '22004'
ERROR_IN_ASSIGNMENT = '22005'
INVALID_DATETIME_FORMAT = '22007'
DATETIME_FIELD_OVERFLOW = '22008'
INVALID_TIME_ZONE_DISPLACEMENT_VALUE = '22009'
ESCAPE_CHARACTER_CONFLICT = '2200B'
INVALID_USE_OF_ESCAPE_CHARACTER = '2200C'
INVALID_ESCAPE_OCTET = '2200D'
ZERO_LENGTH_CHARACTER_STRING = '2200F'
MOST_SPECIFIC_TYPE_MISMATCH = '2200G'
SEQUENCE_GENERATOR_LIMIT_EXCEEDED = '2200H'
NOT_AN_XML_DOCUMENT = '2200L'
INVALID_XML_DOCUMENT = '2200M'
INVALID_XML_CONTENT = '2200N'
INVALID_XML_COMMENT = '2200S'
INVALID_XML_PROCESSING_INSTRUCTION = '2200T'
INVALID_INDICATOR_PARAMETER_VALUE = '22010'
SUBSTRING_ERROR = '22011'
DIVISION_BY_ZERO = '22012'
INVALID_PRECEDING_OR_FOLLOWING_SIZE = '22013'
INVALID_ARGUMENT_FOR_NTILE_FUNCTION = '22014'
INTERVAL_FIELD_OVERFLOW = '22015'
INVALID_ARGUMENT_FOR_NTH_VALUE_FUNCTION = '22016'
INVALID_CHARACTER_VALUE_FOR_CAST = '22018'
INVALID_ESCAPE_CHARACTER = '22019'
INVALID_REGULAR_EXPRESSION = '2201B'
INVALID_ARGUMENT_FOR_LOGARITHM = '2201E'
INVALID_ARGUMENT_FOR_POWER_FUNCTION = '2201F'
INVALID_ARGUMENT_FOR_WIDTH_BUCKET_FUNCTION = '2201G'
INVALID_ROW_COUNT_IN_LIMIT_CLAUSE = '2201W'
INVALID_ROW_COUNT_IN_RESULT_OFFSET_CLAUSE = '2201X'
INVALID_LIMIT_VALUE = '22020'
CHARACTER_NOT_IN_REPERTOIRE = '22021'
INDICATOR_OVERFLOW = '22022'
INVALID_PARAMETER_VALUE = '22023'
UNTERMINATED_C_STRING = '22024'
INVALID_ESCAPE_SEQUENCE = '22025'
STRING_DATA_LENGTH_MISMATCH = '22026'
TRIM_ERROR = '22027'
ARRAY_SUBSCRIPT_ERROR = '2202E'
INVALID_TABLESAMPLE_REPEAT = '2202G'
INVALID_TABLESAMPLE_ARGUMENT = '2202H'
DUPLICATE_JSON_OBJECT_KEY_VALUE = '22030'
INVALID_JSON_TEXT = '22032'
INVALID_SQL_JSON_SUBSCRIPT = '22033'
MORE_THAN_ONE_SQL_JSON_ITEM = '22034'
NO_SQL_JSON_ITEM = '22035'
NON_NUMERIC_SQL_JSON_ITEM = '22036'
NON_UNIQUE_KEYS_IN_A_JSON_OBJECT = '22037'
SINGLETON_SQL_JSON_ITEM_REQUIRED = '22038'
SQL_JSON_ARRAY_NOT_FOUND = '22039'
SQL_JSON_MEMBER_NOT_FOUND = '2203A'
SQL_JSON_NUMBER_NOT_FOUND = '2203B'
SQL_JSON_OBJECT_NOT_FOUND = '2203C'
TOO_MANY_JSON_ARRAY_ELEMENTS = '2203D'
TOO_MANY_JSON_OBJECT_MEMBERS = '2203E'
SQL_JSON_SCALAR_REQUIRED = '2203F'
FLOATING_POINT_EXCEPTION = '22P01'
INVALID_TEXT_REPRESENTATION = '22P02'
INVALID_BINARY_REPRESENTATION = '22P03'
BAD_COPY_FILE_FORMAT = '22P04'
UNTRANSLATABLE_CHARACTER = '22P05'
NONSTANDARD_USE_OF_ESCAPE_CHARACTER = '22P06'

# Class 23 - Integrity Constraint Violation
INTEGRITY_CONSTRAINT_VIOLATION = '23000'
RESTRICT_VIOLATION = '23001'
NOT_NULL_VIOLATION = '23502'
FOREIGN_KEY_VIOLATION = '23503'
UNIQUE_VIOLATION = '23505'
CHECK_VIOLATION = '23514'
EXCLUSION_VIOLATION = '23P01'

# Class 24 - Invalid Cursor State
INVALID_CURSOR_STATE = '24000'

# Class 25 - Invalid Transaction State
INVALID_TRANSACTION_STATE = '25000'
ACTIVE_SQL_TRANSACTION = '25001'
BRANCH_TRANSACTION_ALREADY_ACTIVE = '25002'
INAPPROPRIATE_ACCESS_MODE_FOR_BRANCH_TRANSACTION = '25003'
INAPPROPRIATE_ISOLATION_LEVEL_FOR_BRANCH_TRANSACTION = '25004'
NO_ACTIVE_SQL_TRANSACTION_FOR_BRANCH_TRANSACTION = '25005'
READ_ONLY_SQL_TRANSACTION = '25006'
SCHEMA_AND_DATA_STATEMENT_MIXING_NOT_SUPPORTED = '25007'
HELD_CURSOR_REQUIRES_SAME_ISOLATION_LEVEL = '25008'
NO_ACTIVE_SQL_TRANSACTION = '25P01'
IN_FAILED_SQL_TRANSACTION = '25P02'
IDLE_IN_TRANSACTION_SESSION_TIMEOUT = '25P03'

# Class 26 - Invalid SQL Statement Name
INVALID_SQL_STATEMENT_NAME = '26000'

# Class 27 - Triggered Data Change Violation
TRIGGERED_DATA_CHANGE_VIOLATION = '27000'

# Class 28 - Invalid Authorization Specification
INVALID_AUTHORIZATION_SPECIFICATION = '28000'
INVALID_PASSWORD = '28P01'

# Class 2B - Dependent Privilege Descriptors Still Exist
DEPENDENT_PRIVILEGE_DESCRIPTORS_STILL_EXIST = '2B000'
DEPENDENT_OBJECTS_STILL_EXIST = '2BP01'

# Class 2D - Invalid Transaction Termination
INVALID_TRANSACTION_TERMINATION = '2D000'

# Class 2F - SQL Routine Exception
SQL_ROUTINE_EXCEPTION = '2F000'
MODIFYING_SQL_DATA_NOT_PERMITTED_ = '2F002'
PROHIBITED_SQL_STATEMENT_ATTEMPTED_ = '2F003'
READING_SQL_DATA_NOT_PERMITTED_ = '2F004'
FUNCTION_EXECUTED_NO_RETURN_STATEMENT = '2F005'

# Class 34 - Invalid Cursor Name
INVALID_CURSOR_NAME = '34000'

# Class 38 - External Routine Exception
EXTERNAL_ROUTINE_EXCEPTION = '38000'
CONTAINING_SQL_NOT_PERMITTED = '38001'
MODIFYING_SQL_DATA_NOT_PERMITTED = '38002'
PROHIBITED_SQL_STATEMENT_ATTEMPTED = '38003'
READING_SQL_DATA_NOT_PERMITTED = '38004'

# Class 39 - External Routine Invocation Exception
EXTERNAL_ROUTINE_INVOCATION_EXCEPTION = '39000'
INVALID_SQLSTATE_RETURNED = '39001'
NULL_VALUE_NOT_ALLOWED = '39004'
TRIGGER_PROTOCOL_VIOLATED = '39P01'
SRF_PROTOCOL_VIOLATED = '39P02'
EVENT_TRIGGER_PROTOCOL_VIOLATED = '39P03'

# Class 3B - Savepoint Exception
SAVEPOINT_EXCEPTION = '3B000'
INVALID_SAVEPOINT_SPECIFICATION = '3B001'

# Class 3D - Invalid Catalog Name
INVALID_CATALOG_NAME = '3D000'

# Class 3F - Invalid Schema Name
INVALID_SCHEMA_NAME = '3F000'

# Class 40 - Transaction Rollback
TRANSACTION_ROLLBACK = '40000'
SERIALIZATION_FAILURE = '40001'
TRANSACTION_INTEGRITY_CONSTRAINT_VIOLATION = '40002'
STATEMENT_COMPLETION_UNKNOWN = '40003'
DEADLOCK_DETECTED = '40P01'

# Class 42 - Syntax Error or Access Rule Violation
SYNTAX_ERROR_OR_ACCESS_RULE_VIOLATION = '42000'
INSUFFICIENT_PRIVILEGE = '42501'
SYNTAX_ERROR = '42601'
INVALID_NAME = '42602'
INVALID_COLUMN_DEFINITION = '42611'
NAME_TOO_LONG = '42622'
DUPLICATE_COLUMN = '42701'
AMBIGUOUS_COLUMN = '42702'
UNDEFINED_COLUMN = '42703'
UNDEFINED_OBJECT = '42704'
DUPLICATE_OBJECT = '42710'
DUPLICATE_ALIAS = '42712'
DUPLICATE_FUNCTION = '42723'
AMBIGUOUS_FUNCTION = '42725'
GROUPING_ERROR = '42803'
DATATYPE_MISMATCH = '42804'
WRONG_OBJECT_TYPE = '42809'
INVALID_FOREIGN_KEY = '42830'
CANNOT_COERCE = '42846'
UNDEFINED_FUNCTION = '42883'
GENERATED_ALWAYS = '428C9'
RESERVED_NAME = '42939'
UNDEFINED_TABLE = '42P01'
UNDEFINED_PARAMETER = '42P02'
DUPLICATE_CURSOR = '42P03'
DUPLICATE_DATABASE = '42P04'
DUPLICATE_PREPARED_STATEMENT = '42P05'
DUPLICATE_SCHEMA = '42P06'
DUPLICATE_TABLE = '42P07'
AMBIGUOUS_PARAMETER = '42P08'
AMBIGUOUS_ALIAS = '42P09'
INVALID_COLUMN_REFERENCE = '42P10'
INVALID_CURSOR_DEFINITION = '42P11'
INVALID_DATABASE_DEFINITION = '42P12'
INVALID_FUNCTION_DEFINITION = '42P13'
INVALID_PREPARED_STATEMENT_DEFINITION = '42P14'
INVALID_SCHEMA_DEFINITION = '42P15'
INVALID_TABLE_DEFINITION = '42P16'
INVALID_OBJECT_DEFINITION = '42P17'
INDETERMINATE_DATATYPE = '42P18'
INVALID_RECURSION = '42P19'
WINDOWING_ERROR = '42P20'
COLLATION_MISMATCH = '42P21'
INDETERMINATE_COLLATION = '42P22'

# Class 44 - WITH CHECK OPTION Violation
WITH_CHECK_OPTION_VIOLATION = '44000'

# Class 53 - Insufficient Resources
INSUFFICIENT_RESOURCES = '53000'
DISK_FULL = '53100'
OUT_OF_MEMORY = '53200'
TOO_MANY_CONNECTIONS = '53300'
CONFIGURATION_LIMIT_EXCEEDED = '53400'

# Class 54 - Program Limit Exceeded
PROGRAM_LIMIT_EXCEEDED = '54000'
STATEMENT_TOO_COMPLEX = '54001'
TOO_MANY_COLUMNS = '54011'
TOO_MANY_ARGUMENTS = '54023'

# Class 55 - Object Not In Prerequisite State
OBJECT_NOT_IN_PREREQUISITE_STATE = '55000'
OBJECT_IN_USE = '55006'
CANT_CHANGE_RUNTIME_PARAM = '55P02'
LOCK_NOT_AVAILABLE = '55P03'
UNSAFE_NEW_ENUM_VALUE_USAGE = '55P04'

# Class 57 - Operator Intervention
OPERATOR_INTERVENTION = '57000'
QUERY_CANCELED = '57014'
ADMIN_SHUTDOWN = '57P01'
CRASH_SHUTDOWN = '57P02'
CANNOT_CONNECT_NOW = '57P03'
DATABASE_DROPPED = '57P04'

# Class 58 - System Error (errors external to PostgreSQL itself)
SYSTEM_ERROR = '58000'
IO_ERROR = '58030'
UNDEFINED_FILE = '58P01'
DUPLICATE_FILE = '58P02'

# Class 72 - Snapshot Failure
SNAPSHOT_TOO_OLD = '72000'

# Class F0 - Configuration File Error
CONFIG_FILE_ERROR = 'F0000'
LOCK_FILE_EXISTS = 'F0001'

# Class HV - Foreign Data Wrapper Error (SQL/MED)
FDW_ERROR = 'HV000'
FDW_OUT_OF_MEMORY = 'HV001'
FDW_DYNAMIC_PARAMETER_VALUE_NEEDED = 'HV002'
FDW_INVALID_DATA_TYPE = 'HV004'
FDW_COLUMN_NAME_NOT_FOUND = 'HV005'
FDW_INVALID_DATA_TYPE_DESCRIPTORS = 'HV006'
FDW_INVALID_COLUMN_NAME = 'HV007'
FDW_INVALID_COLUMN_NUMBER = 'HV008'
FDW_INVALID_USE_OF_NULL_POINTER = 'HV009'
FDW_INVALID_STRING_FORMAT = 'HV00A'
FDW_INVALID_HANDLE = 'HV00B'
FDW_INVALID_OPTION_INDEX = 'HV00C'
FDW_INVALID_OPTION_NAME = 'HV00D'
FDW_OPTION_NAME_NOT_FOUND = 'HV00J'
FDW_REPLY_HANDLE = 'HV00K'
FDW_UNABLE_TO_CREATE_EXECUTION = 'HV00L'
FDW_UNABLE_TO_CREATE_REPLY = 'HV00M'
FDW_UNABLE_TO_ESTABLISH_CONNECTION = 'HV00N'
FDW_NO_SCHEMAS = 'HV00P'
FDW_SCHEMA_NOT_FOUND = 'HV00Q'
FDW_TABLE_NOT_FOUND = 'HV00R'
FDW_FUNCTION_SEQUENCE_ERROR = 'HV010'
FDW_TOO_MANY_HANDLES = 'HV014'
FDW_INCONSISTENT_DESCRIPTOR_INFORMATION = 'HV021'
FDW_INVALID_ATTRIBUTE_VALUE = 'HV024'
FDW_INVALID_STRING_LENGTH_OR_BUFFER_LENGTH = 'HV090'
FDW_INVALID_DESCRIPTOR_FIELD_IDENTIFIER = 'HV091'

# Class P0 - PL/pgSQL Error
PLPGSQL_ERROR = 'P0000'
RAISE_EXCEPTION = 'P0001'
NO_DATA_FOUND = 'P0002'
TOO_MANY_ROWS = 'P0003'
ASSERT_FAILURE = 'P0004'

# Class XX - Internal Error
INTERNAL_ERROR = 'XX000'
DATA_CORRUPTED = 'XX001'
INDEX_CORRUPTED = 'XX002'
