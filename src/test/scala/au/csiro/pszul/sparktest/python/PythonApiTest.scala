package au.csiro.pszul.sparktest.python

import org.junit.Assert.assertEquals
import org.junit.Test


class PythonApiTest {

  @Test
  def testVersion(): Unit = {
    assertEquals("0.2.0", PythonApi.getVersion())
  }
}
