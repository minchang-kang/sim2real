import time

from obs_builder import ObservationBuilder
from inference import TorchInferencer as Inference
from motor import MotorController as Controller

# initialize

# main loop
while True:
    start = time.perf_counter()

    command = [0.0, 0.0, 0.0]

    # get data

    obs = ObservationBuilder(command)
    actions = Inference(obs)
    Controller(actions)

    elapsed = time.perf_counter() - start
    time.sleep(max(0.0, 0.01 - elapsed))