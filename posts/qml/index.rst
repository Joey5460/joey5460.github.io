qmake pro file
-----------------
-LIBS += -ltoxcore -ltoxencryptsave
-LIBS += -L/usr/local/lib -lmath
-INSTALLS += target qmldir
-TEMPLATE = app
-TEMPLATE = lib 

specify platform
----------------
.. code-block::

    linux:!android {
        message("* Using settings for Unix/Linux.")
        LIBS += -L/path/to/linux/libs
    }

https://stackoverflow.com/questions/18104716/how-to-specify-libraries-only-for-android-platform-build-in-pro-file

Extending with android
----------------------
https://doc.qt.io/qt-5/qandroidjniobject.html

When importing a module called “org.example.io”, the QML engine will look in one of the import paths and tries to locate the “org/example/io” path with a qmldir.

Web Assembly
------------
https://stackoverflow.com/questions/59545455/web-assembly-typeerror-networkerror-when-attempting-to-fetch-resource

emrun --no_browser --port 8080 .

.. code-block::

    Page {
        id: root
        property string inConversationWith
    }

Debug
------
https://doc.qt.io/qt-5/qtquick-debugging.html

.. code-block::

    function f(a, b) {
      console.log("a is ", a, "b is ", b);
    }

connect
--------
https://felgo.com/doc/felgo-qml-communication-basics/

https://forum.qt.io/topic/99556/communication-between-qml-objects

Element
--------
AppliationWindow
Page
Header
Label

anchors.fill: parent
layout

