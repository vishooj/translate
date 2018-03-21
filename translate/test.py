from py4j.java_gateway import JavaGateway
gateway = JavaGateway()                   # connect to the JVM

addition_app = gateway.entry_point        # get the AdditionApplication instance
print(addition_app.addition(1, 2))    # call the addition method