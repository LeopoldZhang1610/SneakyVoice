# SneakyVoice Attack Framework
The running audio samples are in the uploaded folder(/Supplementary Material/example")

This document describes the detailed process of attacking the TTS model and how to use our framework for generating adversarial perturbations in voice cloning and voice conversion tasks.

## 1. Original Code

This project is based on the [Coqui TTS model](https://github.com/coqui-ai/TTS).

## 2. Directory Structure

The project structure is as follows:

#Directory Structure
|- notebooks/       (Jupyter Notebooks for model evaluation, parameter selection and data analysis.)
|- utils/           (common utilities.)
|- TTS
    |- bin/             (folder for all the executables.)
      |- train*.py                  (train your target model.)
      |- ...
    |- tts/             (text to speech models)
        |- layers/          (model layer definitions)
        |- models/          (model definitions)
        |- utils/           (model specific utilities.)
    |- speaker_encoder/ (Speaker Encoder models.)
        |- (same)
    |- vocoder/         (Vocoder models.)
        |- (same)

Make sure to download the original TTS code and the required pre-trained models from the links provided in the repository.

## 3. Detailed Process

### 3.1 Generating Adversarial Perturbations for Voice Cloning (XTTS)

#### 3.1.1 Model Gradient Maintenance

To improve computing efficiency and save resources, some gradients are turned off by default in the original TTS implementation. However, these gradients are necessary when generating adversarial perturbations. Therefore, we ensure that these gradients are maintained during the attack generation process.

#### 3.1.2 Code Modifications to Create Adversarial Perturbations

We have modified the following files to implement adversarial perturbations for voice cloning:

- `/path/to/your/file/TTS/utils/synthesizer.py`
- `/path/to/your/file/TTS/tts/utils/managers.py`
- `/path/to/your/file/TTS/voice_cloning_adv.py` (This file does not exist in the original project.)

The modifications in these files are designed to inject adversarial perturbations into the voice cloning process. You can generate adversarial voice samples by running the script `voice_cloning_adv.py`.

### 3.2 Generating Adversarial Perturbations for Voice Conversion (FreeVC)

#### 3.2.1 Model Gradient Maintenance

Similar to the voice cloning process, we also ensure that the necessary gradients are maintained during the voice conversion attack.

#### 3.2.2 Code Modifications to Create Adversarial Perturbations

The following files were modified to implement adversarial perturbations for voice conversion:

- `/path/to/your/file/TTS/vc/models/freevc.py`
- `/path/to/your/file/TTS/voice_conversion_adv.py` (This file does not exist in the original project.)

These changes allow for the generation of adversarial voice conversion samples, which can be tested using the script `voice_conversion_adv.py`.

## 4. Usage

1. **Set Up the Project:**
   - Make sure to download the required code and pre-trained models.
   - Modify the paths in the code to point to the correct locations of your models and input data.

2. **Running the Scripts:**
   - To generate adversarial perturbations for **voice cloning**, run the following command:
   
     ```bash
     python voice_cloning_adv.py
     ```
   
   - To generate adversarial perturbations for **voice conversion**, run the following command:
   
     ```bash
     python voice_conversion_adv.py
     ```

3. **Output:**
   - The adversarial outputs will be saved in the specified output directory. You can inspect the generated voice samples and compare them with the original outputs to evaluate the impact of the adversarial attack.

## 5. Acknowledgments

This project builds upon the open-source [Coqui TTS model](https://github.com/coqui-ai/TTS), and we acknowledge the original authors for their contributions. Our modifications aim to explore the robustness of TTS systems under adversarial conditions.


