import cv2
import numpy as np

# import pywt
from PIL import Image

class Transform:
    name: str
    
    def __init__(self) -> None:
        pass

    def __call__(self,image:Image.Image)->Image.Image:
        raise NotImplementedError("Transform not implemented")
    
class NoTransform(Transform):
    name = "NoTransform"
    
    def __call__(self, image: Image.Image):
        return image


class GrayTransform:
    name: str

    def __init__(self) -> None:
        """
        input format: Image.Image
        output format: Image.Image
        """
        pass

    def image_to_numpy(self, image: Image.Image):
        return np.asarray(image.convert("L"), dtype=np.uint8)

    def numpy_to_image(self, image: np.ndarray) -> Image.Image:
        return Image.fromarray(np.uint8(self.range(image) * 255))

    def range(self, image: np.ndarray) -> np.ndarray:
        """
        range image into [0,1]

        Args:
            image (np.ndarray): image

        Returns:
            np.ndarray: image with range
        """
        image = image - np.min(image)
        image = image / np.max(image)
        return image

    def __call__(self, image: Image.Image) -> Image.Image:
        image = self.image_to_numpy(image)
        image = self.core(image)
        return self.numpy_to_image(image)

    def core(self, image: np.ndarray) -> np.ndarray:
        """
        core algorithm to process image with range [0,1]

        Args:
            image (np.ndarray): input image

        Raises:
            NotImplementedError: tips

        Returns:
            np.ndarray: output image
        """
        raise NotImplementedError(
            f"Core algorithm in {self.__class__.__name__} is not implemented yet."
        )

    # def wavelet(
    #     self,
    #     img: np.ndarray,
    #     wave: str = "sym4",
    #     level: int = 3,
    #     threshold: float = 0.04,
    # ) -> np.ndarray:
    #     coeffs = pywt.wavedec2(data=img, wavelet=wave, level=level)
    #     list_coeffs = []
    #     for i in range(1, len(coeffs)):
    #         list_coeffs_ = list(coeffs[i])
    #         list_coeffs.append(list_coeffs_)

    #     for r1 in range(len(list_coeffs)):
    #         for r2 in range(len(list_coeffs[r1])):
    #             list_coeffs[r1][r2] = pywt.threshold(
    #                 list_coeffs[r1][r2], threshold * np.max(list_coeffs[r1][r2])
    #             )

    #     rec_coeffs = []
    #     rec_coeffs.append(coeffs[0])

    #     for j in range(len(list_coeffs)):
    #         rec_coeffs_ = tuple(list_coeffs[j])
    #         rec_coeffs.append(rec_coeffs_)

    #     return pywt.waverec2(rec_coeffs, wave)


class LogTransform(GrayTransform):
    name = "log"

    def __init__(self, v: float = 1.0, **kwargs):
        super().__init__(**kwargs)
        self.v = v

    def core(self, image: np.ndarray) -> np.ndarray:
        image = self.range(image)
        return np.log(1.0 + self.v * image)


class GammaTransform(GrayTransform):
    name = "gamma"

    def __init__(self, gamma: float = 1.0, **kwargs):
        super().__init__(**kwargs)
        self.gamma = gamma

    def core(self, image: np.ndarray) -> np.ndarray:
        image = self.range(image)
        return np.power(image, self.gamma)


class HETransform(GrayTransform):
    name = "he"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def core(self, image: np.ndarray) -> np.ndarray:
        return cv2.equalizeHist(image)


class AHETransform(GrayTransform):
    name = "ahe"

    def __init__(self, tileGridSize: tuple[int, int] = (12, 12), **kwargs):
        super().__init__(**kwargs)
        self.clahe = cv2.createCLAHE(tileGridSize=tileGridSize)

    def core(self, image: np.ndarray) -> np.ndarray:
        return self.clahe.apply(image)


class CLAHETransform(GrayTransform):
    name = "clahe"

    def __init__(
        self, clipLimit: float = 4.0, tileGridSize: tuple[int, int] = (12, 12), **kwargs
    ):
        super().__init__(**kwargs)
        self.clahe = cv2.createCLAHE(clipLimit=clipLimit, tileGridSize=tileGridSize)

    def core(self, image: np.ndarray) -> np.ndarray:
        return self.clahe.apply(image)
