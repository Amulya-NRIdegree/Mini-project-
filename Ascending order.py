{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyNZu1mQta0KbtbTgeoBcwtm",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/Amulya-NRIdegree/Mini-project-/blob/main/Ascending%20order.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 6,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "iddTlP3uME9v",
        "outputId": "78b832a6-7bdc-472d-9e79-f1610bb3ab6c"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "In ascending order: [3, 6, 7, 8, 10, 13]\n"
          ]
        }
      ],
      "source": [
        "#list of elements to sort\n",
        "L1= [6,8,3,7,10,13]\n",
        "L2=[]\n",
        "\n",
        "#loop to sort the elements\n",
        "for i in range (len(L1)):\n",
        "\n",
        "      min_val= L1 [0]\n",
        "      for j in range (1,len (L1)):\n",
        "          if L1[j] < min_val:\n",
        "             min_val= L1 [j]\n",
        "\n",
        "      L2.append( min_val)\n",
        "      L1.remove( min_val)\n",
        "\n",
        "print (\"In ascending order:\",L2)"
      ]
    }
  ]
}