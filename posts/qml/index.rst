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

qmldir
------

.. code-block::

    module example.io #(uri/path)
    plugin plugin #(libplugin)

qmlRegisterType<cppclass><uri,1,0,"qmlcppclass">

import module(uri) 1.0

connect
--------
https://felgo.com/doc/felgo-qml-communication-basics/

https://forum.qt.io/topic/99556/communication-between-qml-objects

Element
--------
AppliationWindow/item/page/rectangle

Item

- width
- height
- visible
  
Page 

- header

Label

- text

StactView

ToolBar

Drawer

ListView_

    - model: ListModel/QAbastractModel
    - delegate: ItemDelegate The index is exposed as an accessible index property. 

.. _ListView: https://doc.qt.io/qt-5/qml-qtquick-listview.html


Variant
-------
property string currentContact : ""

Property
---------
write read notify

.. code-block::

    model: SqlChatModel{
        recipient: inConversationWith
    }


func: eg model.sendMessage


Layout
------
- anchors.fill: parent
- anchors.centerIn: parent  
- Layout.fillWidth

- layout

Parent is null in ListView delegate after upgrade to Qt 5.15

https://stackoverflow.com/questions/63767669/parent-is-null-in-listview-delegate-after-upgrade-to-qt-5-15

Componet
--------
https://doc.qt.io/archives/qt-4.8/qml-component.html

Component.onCompleted: {}
Component.onDestruction:{}

.. code-block::

    Loader {
            id: dialLoader

            anchors.left: parent.left
            anchors.right: parent.right
            anchors.top: parent.top
            anchors.bottom: analogButton.top

            onLoaded: {
                binder.target = dialLoader.item;
            }
    }

    Binding {
            id: binder

            property: "speed"
            value: speed
    }

Signals(call back)
-------------------
https://doc.qt.io/archives/qt-4.8/qmlevents.html

id.singalFunc.connect(slotFunc)

.. code-block::

       Rectangle {
            id: relay

            signal send(string person, string notice)
            onSend: console.log("Send signal to: " + person + ", " + notice)

            Component.onCompleted: {
                relay.send.connect(sendToPost)
                relay.send.connect(sendToTelegraph)
                relay.send.connect(sendToEmail)
                relay.send("Tom", "Happy Birthday")
            }

            function sendToPost(person, notice) {
                console.log("Sending to post: " + person + ", " + notice)
            }
            function sendToTelegraph(person, notice) {
                console.log("Sending to telegraph: " + person + ", " + notice)
            }
            function sendToEmail(person, notice) {
                console.log("Sending to email: " + person + ", " + notice)
            }
        }

https://doc.qt.io/qt-5/qml-qtqml-connections.html#details

https://doc.qt.io/qt-5/qtqml-syntax-signals.html
