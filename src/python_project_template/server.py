import litserve as ls


# (STEP 1) - DEFINE THE API (compound AI system)
class SimpleLitAPI(ls.LitAPI):
    def setup(self, device):
        # setup is called once at startup. Build a compound AI system (1+ models), connect DBs, load data, etc...
        self.model = lambda x: x**2

    def decode_request(self, request):
        # Convert the request payload to model input.
        return request["input"] 

    def predict(self, x):
        # Easily build compound systems. Run inference and return the output.
        output = self.model(x)
        return {"output": output}

    def encode_response(self, output):
        # Convert the model output to a response payload.
        return {"output": output} 

# (STEP 2) - START THE SERVER
if __name__ == "__main__":
    # scale with advanced features (batching, GPUs, etc...)
    server = ls.LitServer(SimpleLitAPI(), accelerator="auto", max_batch_size=1)
    server.run(port=8000)
