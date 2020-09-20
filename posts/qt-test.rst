.. code::

    class TestDemo: public QObject
    {
        public Q_SLOTS:
            void startTest()
            {
                QTest::qExec(this)
            }
        private Q_SLOTS:
            void test1()
            {
            }    
        
    }





