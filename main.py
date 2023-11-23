from flask import Flask,render_template,request
from flask_ngork import run_with_ngork

import torch
from diffusers import StableDiffusionPipeline

import base64
from io import BytesIO


pipe = StableDiffusionPipeline.from_pertrained(f)