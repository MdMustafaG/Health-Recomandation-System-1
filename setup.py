from setuptools import setup, find_packages

setup(
    name="health-recommendation-system",
    version="1.0.0",
    author="Mahboob Attar",
    author_email="freespace.alltime@gmail.com",
    description="A Health Recommendation System using Flask and SVM (scikit-learn).",
    packages=find_packages(),
    install_requires=[
        "flask",
        "numpy",
        "pandas",
        "scikit-learn",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
)
