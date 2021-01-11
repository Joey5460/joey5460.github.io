c++ compile
-----------
gcc -I/usr/local/include xxx.c -o xxx -L/usr/local/lib -Wl,-rpath, DIR

https://stackoverflow.com/questions/480764/linux-error-while-loading-shared-libraries-cannot-open-shared-object-file-no-s

https://stackoverflow.com/questions/6562403/i-dont-understand-wl-rpath-wl

compile libsodium 
--------------------

configure

.. code-block::

	./configure --prefix=~/projs/user/local

tox complile
-------------
export PKG_CONFIG_PATH=~/projs/usr/local/lib/pkgconfig
mkdir build
cd build
cmake ..

sample
------

store key

https://wiki.tox.chat/developers/client_examples/echo_bot

qml
-----
onClicked:{}

property string currentContact : ""

signal pushChatPage(string name)

The custom model must reimplement the following methods to enable read-only access to the data from QML:

QSqlQueryModel_ (Read-only Data Model)

- roleNames()
- data()

.. _QSqlQueryModel: https://doc.qt.io/qt-5/qtquick-modelviewsdata-cppmodels.html#read-only-data-model

signal
======

cpp signal can be even connected to qml

.. code-block::

    EzTox{
        id: chat
            Component.onCompleted: {
            chat.friendMessageReceived.connect(onMsgReceived)
        }
        function onMsgReceived(id, notice) {
            console.log("Sending to "+id+ ","+notice);
        }
    }
    Connections {
        target: contactPage
        function onPushChatPage(name)  {
            stackView.push("./ConversationPage.qml", {inConversationWith: name});
            chat.run();
        }
    }

sql
----

.. code-block::

    QSqlQuery query;
    QString sql = "DELETE FROM Contacts WHERE name = '" + name + "'";
    if (!query.exec(sql))
        qFatal("delete failed: %s", qPrintable(query.lastError().text()));


vim
----
in .vimrc

autocmd FileType qml noremap <F5> :wa <CR>: !qmlscene main.qml <CR>

https://andrew.stwrt.ca/posts/vim-ctags/

tmux
-----
in .tmux.conf

bind-key -n F5 run "qmlscene main.qml"

cmd
----
grep str -r . -i -n




