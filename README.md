# docker-template

```bash
pre-commit install
```

# Introduction

Turn text into lifelike spoken audio using Azure Speech Services's TTS

## Getting Started

1. **Clone the repository**:

   ```bash
   git clone https://github.com/your-username/my-template-repo.git
   cd my-template-repo

## Prerequisites

Before you get started, here's a list of prerequisites:

* A subscription key for the Speech service. See [Try the speech service for free](https://docs.microsoft.com/azure/cognitive-services/speech-service/get-started).
* On Windows and Linux Python 3.6 or later needs to be installed. On Mac, minimum version for Python is 3.7. Downloads are available [here](https://www.python.org/downloads/).
* The Python Speech SDK package is available for Windows (x64 and x86), Mac x64 (macOS X version 10.14 or later), Mac arm64 (macOS version 11.0 or later), and [specific Linux distributions and target architectures](https://docs.microsoft.com/azure/cognitive-services/speech-service/speech-sdk?tabs=linux).
* On Ubuntu or Debian, run the following commands for the installation of required packages:
  ```sh
  sudo apt-get update
  sudo apt-get install libssl-dev libasound2
  ```

* On RHEL or CentOS, run the following commands for the installation of required packages:
  ```sh
  sudo yum update
  sudo yum install alsa-lib openssl python3
  ```

  * See also [how to configure RHEL/CentOS 7 for Speech SDK](https://docs.microsoft.com/azure/cognitive-services/speech-service/how-to-configure-rhel-centos-7).

* On Windows you need the [Microsoft Visual C++ Redistributable for Visual Studio 2017](https://support.microsoft.com/help/2977003/the-latest-supported-visual-c-downloads) for your platform.

## Get the Speech SDK Python Package

**By downloading the Microsoft Cognitive Services Speech SDK, you acknowledge its license, see [Speech SDK license agreement](https://aka.ms/csspeech/license).**

The Cognitive Services Speech SDK Python package can be installed from [pyPI](https://pypi.org/) using this command:

```sh
pip install azure-cognitiveservices-speech
```

Note: this tutorial will not work without changes for any version earlier than 1.7.0 of the SDK.