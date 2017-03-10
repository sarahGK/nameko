# nameko
a practice with micro-service package nameko and sqlalchemy

1. What pakages do you need?(For Mac OSX)
   Python3,RabbitMQ,nameko and nameko-sqlalchemy

2. How to start the "blackjack" application?
   Follow the instructions listed bellow which are mainly terminal command lines.
   
   $ rabbitmq-server (many Nameko’s built-in features rely on RabbitMQ)

             RabbitMQ 3.6.4. Copyright (C) 2007-2016 Pivotal Software, Inc.
  ##  ##      Licensed under the MPL.  See http://www.rabbitmq.com/
  ##  ##
  ##########  Logs: /usr/local/var/log/rabbitmq/rabbit@localhost.log
  ######  ##        /usr/local/var/log/rabbitmq/rabbit@localhost-sasl.log
  ##########
              Starting broker...
 completed with 10 plugins.
 
 -------------------------------------------------------------------------------------
   Then open another terminal window
   $ nameko run service
   .......
   .......
   Connected to amqp://guest:**@127.0.0.1:5672//
--------------------------------------------------------------------------------------

   Then open another terminal window to play the game
   $nameko shell
   
Nameko Python 3.5.2 (v3.5.2:4def2a2901a5, Jun 26 2016, 10:47:25) 
[GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] shell on darwin
Broker: b'amqp://guest:guest@localhost'
>>> 
   
----------------------------------------------------------------------------------------

   Under nameko shell, use these three command lines to play BlackJack
   >>> n.rpc.blackjack.start()
   >>> n.rpc.blackjack.hit()
   >>> n.rpc.blackjack.stick()

