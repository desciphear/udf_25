import realtime_plot_window
import webcam2rgb
import time


if __name__ == "__main__":

    realTimeWindow = realtime_plot_window.RealtimeWindow("Morse Decoder")


    def hasData(retval, data):
        
        luminance = ( (0.2126*data[2]) + (0.7152*data[1]) + (0.0722*data[0]) )
        # Pass signal to realtime window
        realTimeWindow.addData(luminance)

  
    camera = webcam2rgb.Webcam2rgb()
    
    realTimeWindow.decoder.timerStart = time.time()
    camera.start(callback = hasData, cameraNumber=0)
    print("Camera Sample Rate: ", camera.cameraFs(), "Hz")
    realtime_plot_window.plt.show()
    camera.stop()

   
    timeElapsed = time.time() - realTimeWindow.decoder.timerStart
    print('\n Measured Sampling Rate: ' + str(realTimeWindow.decoder.totalSampleCount / timeElapsed))

    # Print Sequences
    print('\nSequence Detected:')  
    print(realTimeWindow.decoder.morseSequence)
    print('\nDecoded Morse Code Sequence: '+ realTimeWindow.decoder.decodedLetters )


   



