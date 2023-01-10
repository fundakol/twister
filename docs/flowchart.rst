Should be executed
==================

In twister test can end after building or after building and executing.
Below flowchart shows how it is determined if test should be executed or not.

.. mermaid::

    flowchart TD
        id1(Check if test should be executed\nor only build)
        S(Start test) --> BUILD
        BUILD[Build source code] --> DID_BUILD_PASS
        DID_BUILD_PASS{Did build\npass?} -- Yes --> IS_BUILD_ONLY
        DID_BUILD_PASS -- No --> ERROR
        IS_BUILD_ONLY{twister_config.\nbuild_only} -- True --> DO_NOT_EXECUTE[Do not execute]
        IS_BUILD_ONLY -- False --> IS_DEVICE_TESTING{"twister_config.\ndevice_testing"}
        IS_DEVICE_TESTING -- True --> IS_TYPE_MCU{platform.\ntype == mcu}
        IS_DEVICE_TESTING -- False --> RUNNABLE{specification.\nrunnable}
        IS_TYPE_MCU -- False --> DO_NOT_EXECUTE
        IS_TYPE_MCU -- True --> RUNNABLE
        RUNNABLE -->|False| DO_NOT_EXECUTE
        RUNNABLE -->|True| EXECUTE[Execute]
        DO_NOT_EXECUTE --> IS_PYTEST
        IS_PYTEST{Is pytest test?} -->|Yes| SKIP[SKIPPED]
        IS_PYTEST -->|No| PASSED[PASSED]
        EXECUTE --> DID_TEST_PASS{Did test pass?}
        DID_TEST_PASS -- Yes --> PASSED
        DID_TEST_PASS -- No --> FAILED
