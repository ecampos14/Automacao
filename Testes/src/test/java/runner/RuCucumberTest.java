package runner;

import org.junit.runner.RunWith;

import cucumber.api.CucumberOptions;
import cucumber.api.junit.Cucumber;

@RunWith(Cucumber.class)
@CucumberOptions(
		plugin = {},
		features = "Testes/resources/features",
		tags = {"~@ignore"},
		glue = {"steps"}
		
)
public class RuCucumberTest {

}
