# nextlab_data
Data pipeline for Next lab at McNair.

This repository is intended for any consumer of Next lab data. The code in sensordata_publishers runs on the raspberry pi and transmits data to the MQTT cloud message broker. 

For documentation on what MOTT is and how to implement clients, please refer to http://www.steves-internet-guide.com/mqtt/. For examples of client subscribers that work out of the box, use nextdatasubscriber.py for Python and javascriptsubscriberexample.html for browser javascript. If you're using a different language, a client library probably exists for it. 

