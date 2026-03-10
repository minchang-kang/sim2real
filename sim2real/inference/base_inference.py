# sim2real/inference/base_inferencer.py

import torch
import numpy as np

from rsl_rl.moduls import ActorCritic


class BaseInferencer:
    def infer(self, obs: np.ndarray) -> np.ndarray:
        raise NotImplementedError


class TorchInferencer(BaseInferencer):
    def __init__(self, cfg):
        self._cfg = cfg
        self._policy = torch.load(self._cfg["policy_path"])["model_state_dict"]
        self._actor_critic = self._initialize_model(self._policy)

        super.__init__()
    
    def _initialize_model(self, model_state_dict):
        model = ActorCritic(
            num_actor_obs=16,
            num_critic_obs=16,
            num_actions=2,
            actor_hidden_dims=[128, 128, 128],
            critic_hidden_dims=[128, 128, 128],
            activation="elu",
        )
        model.load_state_dict(model_state_dict)
        model.eval()
        return model

    def infer(self, obs: np.ndarray):
        with torch.inference_mode():
            obs = torch.from_numpy(obs).float()
            action = self._actor_critic.act(obs).detach().numpy()
        
        return action
    

class ONNXInferencer(BaseInferencer):
    def infer(self):
        pass

    
class TFLiteInferencer(BaseInferencer):
    def infer(self):
        pass