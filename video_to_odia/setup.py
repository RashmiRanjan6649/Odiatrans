from setuptools import setup, find_packages

setup(
    name="video_to_odia",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "moviepy",
        "SpeechRecognition",
        "googletrans==4.0.0-rc1"
    ],
    entry_points={
        "console_scripts": [
            "video_to_odia=video_to_odia.__main__:main",
        ],
    },
    description="A tool to transcribe and translate videos from English to Odia.",
    author="Rashmi Ranjan Sahoo",
    author_email="your_email@example.com",
    url="https://github.com/yourgithub/video_to_odia",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
