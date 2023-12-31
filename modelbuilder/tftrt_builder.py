import os
from tensorflow.python.compiler.tensorrt import trt_convert as trt


class TFTRTBuilder:
    """
    Class to create a TensorFlow-TensorRT (TF-TRT) optimized model from an existing TensorFlow SavedModel.
    """


    def convert_and_save_model(self, tf_model_path: str, output_path: str, precision: str, batch_size: int):

        """
        Convert the TensorFlow model to TF-TRT optimized model and save it.

        Args:
            tf_model_path (str): The path to the original TensorFlow SavedModel.
            output_path (str): The directory where the optimized TF-TRT model will be saved.
            precision (str): The precision mode for optimization ('FP16' or 'FP32').
            batch_size (int): The batch size for inference.
        """

        """
        Create the TensorFlow-TensorRT optimized model and save it to the output directory.
        """

        if precision == "FP16":
            conversion_params = trt.DEFAULT_TRT_CONVERSION_PARAMS._replace(precision_mode=trt.TrtPrecisionMode.FP16)
        else:
            conversion_params = trt.DEFAULT_TRT_CONVERSION_PARAMS._replace(precision_mode=trt.TrtPrecisionMode.FP32)

        converter = trt.TrtGraphConverterV2(input_saved_model_dir=tf_model_path,
                                            conversion_params=conversion_params)
        converter.convert()
        converter.save(output_path + '/TFTRT_' + precision + '/')
