step 1
-------
.. listing:: qmlplugin/cpp/fileio.h
   :start-after: //! [0]
   :end-before: //! [0]


.. code-block::

    qmlRegisterType<FileIO>(uri, 1, 0, "FileIO");

FileIO with <> is our class name. FileIO with "" is our element name used in qml 
