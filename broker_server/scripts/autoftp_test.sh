#!/bin/sh

curl -i -H "Accept: text/plain" -H "Content-Type:application/json" -X POST -d '{"autoftpfun":"167F_FTP","TxCod":"167","BrkCod":"7000","BrokerNoLen":"04","BrokerNo":"7000","TakeBorrowDateLen":"07","TakeBorrowDate":"1051017","Option1Len":"01","Option1":"1","FileNo":"000001"}' http://localhost:5100/fsr
