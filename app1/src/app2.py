##################################################################
#   This python application will react to http trigger           #
#      to launch test on code  on each test_case                 #
#      1/ first validate the code with test case stored on kafka #
#      2/ if validation ok running perf                          #
#      2.1/ trig the monitoring                                  #
#      2.2/ for each test case                                   #
#      2.2.1/ run test                                           #
#                                                                #
#     Do not change this file  or just for desactivate           #
#   some problems case                                           # 
#       The scorer will use its copy on your code                #
#                                                                #
# modules required : flask, kafka-python, subprocess 
##################################################################
import io
import max# stupid example to ensure mechanism work 
from kafka import KafkaConsumer 
from kafka import TopicPartition
#  add flask for put in rest api service
# add subprocess to launch start monitoring

### temporary part waiting flask impementation to use http call#####
test_cases={
    'max':['perf1']
    }
problems=['max'] # temporary use call http to drive it later 

###########################################################


for p in problems:
    ## validation part
    
    work=getattr(globals()[p],"run")
    #fetching from kafka all valid test/result message run one
    topic_valid=p+"_valid"
    consumer = KafkaConsumer(topic_valid,group_id="participant_a",auto_offset_reset="earliest",consumer_timeout_ms=1000) # begin fetch to first message of topic at each launch 
    
    print("consuming examples")
    valid_success=True
    for msg in consumer :
        value=msg.value.decode("utf-8")# examples are stored in binary
        m=value.split("#@###@#") # char sequence to separate input and theaorical output
        result=work(m[0])
        print("return ["+result+"] must be ["+m[1]+"]")
        if result==m[1] :
            print("success")
        else:
            print("test"+str(msg.key)+" waiting "+m[1])
            valid_success=False

    print("stop consuming examples")

    if valid_success:
        # do we need to store when the perf test is running and with speed results ?
        ##  # trig start monitoring cpu/pram ( start.sh )
        for tc in test_cases[p]:
            topic=p+tc
            consumer = KafkaConsumer(topic,group_id="participant_a",auto_offset_reset="earliest",consumer_timeout_ms=1000) # begin fetch to first message of topic
            for msg in consumer:
                value=msg.value.decode("utf-8")
                work(value)
            # no push on topic no needed
        ## # trig stop monitoring

        
        
           
            
        
        



    
    







