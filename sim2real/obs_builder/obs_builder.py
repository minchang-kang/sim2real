# sim2real/obs_builder/obs_builder.py

import numpy as np

class ObservationBuilder:
    def build(self, command: np.ndarray) -> np.ndarray:
        # 예: normalize, clip, concatenate
        obs = np.zeros(16)
        
        # command
        obs[:3] = command
        """
        # lin vel
        obs[:6] = 
        # ang vel
        obs[:9] = 
        # gravity
        obs[:12] = 
        # wheel vel
        obs[12:14] = 
        # previous action
        obs[14:16] = 
        """
        return obs