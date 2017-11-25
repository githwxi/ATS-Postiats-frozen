// ====== ====== //

/**
 * Sample React Native App
 * https://github.com/facebook/react-native
 * @flow
 */

// ====== ====== //

import
React,
{
  Component
} from 'react';

import
{
  Platform,
  StyleSheet,
  Text,
  View,
  Alert,
  Button,
} from 'react-native';

// ====== ====== //

import
{
  thePrime_fnext
} from "./atscc2js/sieve_dats_all.js";

// ====== ====== //

function
Start_handle_press
  (/*void*/)
{
//
do_next
(
1, thePrime_fnext()
) ; return /*void*/;
//
//
} // Start_handle_press

function
do_next(n, fnext)
{
//
const
message_text =
`Prime(${n}) = ${fnext()}`
//
Alert.alert
(
"Sieve",
message_text,
[
  {
    text: 'Next'
  , onPress: () => do_next(n+1, fnext)
  },
  {
    text: 'Stop'
  , onPress: () => do_stop(/*cancel*/)
  }
],
{ cancelable: false }
) // Alert.alert
}

function
do_stop(/*cancel*/) { return; }

// ====== ====== //

export
default
class App
extends Component<{}> {
  render() {
    return (
      <View style={styles.container}>
        <Text style={styles.welcome}>
          { "Welcome to\n"
	  + "React-Native Sieve!"
	  }
        </Text>
	<Button
	  title="Start"
	  onPress={ () => Start_handle_press() }
	></Button>
      </View>
    );
  }
}

// ====== ====== //

const
styles =
StyleSheet.create
(
{
  container: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
    backgroundColor: '#F5FCFF',
  },
  welcome: {
    fontSize: 20,
    textAlign: 'center',
    margin: 10,
  },
});

// ====== ====== //
