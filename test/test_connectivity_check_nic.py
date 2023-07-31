# coding: utf-8

"""
    AssistedInstall

    Assisted installation  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


import unittest
import datetime

import openshift_assisted_service
from openshift_assisted_service.models.connectivity_check_nic import ConnectivityCheckNic  # noqa: E501
from openshift_assisted_service.rest import ApiException

class TestConnectivityCheckNic(unittest.TestCase):
    """ConnectivityCheckNic unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ConnectivityCheckNic
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ConnectivityCheckNic`
        """
        model = openshift_assisted_service.models.connectivity_check_nic.ConnectivityCheckNic()  # noqa: E501
        if include_optional :
            return ConnectivityCheckNic(
                name = '', 
                mac = '', 
                ip_addresses = [
                    'CB020842930cc01FFCCfeEe150AC32DcAEc8a83DDD7dBF7567C88195ffcea31C1b:dCBC78DEacF0EA282B47feD6d3dAcFFF9545Be98904E6Ea0E19c0Dfc8dFCF8D577bFC48763F474F07D:c99aEC7c1B2E2B626CB508AEcfc0DD56fDA8A7bFB9A4060eAf297f7cD76bc7939fb0E225975a124d2C66d153097199E828A660Ce5CCc93eD7e3ECfF17e13DE2c7dDd66AC8dd3CfCcd6AEAbCd3b52cDe3:c9Fba4Ae4230A0fC9311b131ADae9f531cBB2dA2AEf8070bEeCA6162BfA9bC3:F1000747701d9308a14FbC5f1dCDC8c0A78:5b9:48A6f7C8aCd1C13E4ce7d55838a2D505577Bd2b397AfdCD16ae5BAF7762F9e19ed6f0bAC1c959d1:835b7d7bAc6892A374a47AaE3178484CE59D3fcAbAcA4fDbcBDB0816E3157f3370aBaDAcC1:aBdb980c9a25eAC4E9c2EccBD959cA0260Da9FBE4cDcEe2c73aEDd61eAC556afC244cd3737dC4A0F67dD86AdD861F325bDA85DF15fbaD8eEc283E54a23a20EEFEBcB9FbeDf8e6dba1fc35eD18BAb6D0125639DC6C2723Fdca1C:5949bbA20a00A4cc27Cba2aB89883C333eb18C9E8CE88C8CacB6d3108a013dda1e9b672afe5BaD6573A5aa80c8eAFf548aBfc33Da9AC4F4A3Ed5cE7FBE4239AC:D4BEF471aE9526F8bDEf8a71DF01fDeAfAf1E5CdDd54b0FCe4b:Fc4DE97f0CaabA76D19eCBf75Ae9a9C894AdBebe2Bb20Effd9a039dA4bfB57E47Cd62A2C5EEF8D90DDDF84BA:6bf0F1fc7aBDC85f74074CF79C7d4cb9E24Efab1047c7bf:33ddaba8a9a69F1FA7c5f89bD760CD2E7aEFE25bB02fAfbaB7939914B088A2DD5eBEbAe8A6a1d97C0e02A56aCD3b4cc78e8767d274:DDabdAa8dBDbBB32542cEd3CFE920908f649DF48388E96FDA8F4Cb17B985e4706769Df4b20cbc9ce4Af26557B1FCA3DDF:BF6b3f6bdEbAbD7BcAcEC2DeD0e9FFEdb2bcCe4346c7Cbd4681a13BDAdEddeEEFCb4fB81c2D92bAF3E4cc2686d40dF8A30bC03342AFb6bDDF7D2C0B1A2cD79B5Ba0bAEfDD2E9:C249BC34DBB1aA73DDF0054C16aa46a5aeDDb928446cBd0f19d7fb89cAF29b5FF4dd4dE4CaDF7B26FFeF8ce5ba0aDAEEfCe31731d5AFf5Cf760eDF3d1bd959eedFeE9BB73dFd8dfF8E00fa13f59:d3e1732Fc2aA91485eF98EAda1e5BCDa6dB55fEe29Af823ABA41E33fD8ffbe56ad5b3fCe5bfc4fCB158a5Fdd0fcc67f8CFd9b8f75DCDCeC1f:3E622E3E0CB7278c847f66E4Eb2A7da9DcD3fe5253a293a26C32cffeeF4aAF4C73Fe5a7caEB01c55Ff33318:FF58fbd0c941A8522b33C15C82056D9dbDBD6f4bA5253feF6bD990ADED1AbDcFD1Facf68bB8F1BA:ceB8ad1FEb2fE969BE9E41708aF44cfbAa4eacD8778d0d2D3Fc8C4c65819b2eeF0c016eBF2BCc799D6d6cA4C30FD7E9F7F2ec38Dc21e6BA15C0D6B497f3cB73E4AdE89AF395BD6Bdf2f96F5cE2AEa5:ceA22dcC0aA13a915d1f77D65c2A150d9dFCe6c385AE7eCbBE9eD2AD37fB8aC164F8E3f0B:d36D652739cDb6620AD69b833dcfdAda7e1bFcDbeB01AdAA0B81F901D1b8af40EF4b3A10B5E8E783e37cD4f1c7b87FE17AB52c02Ea6fcc8aEF0eaEB157e2ae3b5C76CB2Ad9Fba5f97aCd025C6B050c:f3487bfdE9bd7DE2cEa78E3E841aabd9f651a340094b9b52FcB8842D2a15AF0FDc3eDF5f52fffc7Ef25De7Ce15a0cc9beE16eAc4c617eB191AecddeEA09B0039b332cF4Acb031cfa4C5a929d69C1BE5E0AaaF22A821EF36602A4DF00473B31:9F3a59178Ff67CbD0C03C7EeadCBc0e2Afe8b495e12D9019954AB1f00534EAD89bb4E8c9F7b2AB916:67B0edEa5b9a99CDFA7b568B48C8b728fF8Cfda6B06b4Cd26EB4e7eE39f1281B3AF69B62eB9f07Dc409CeA08778c08:dF0cba5d821BFaCe2c3EaE3eda5CBc762accC638579831AfFf4E0F7FA71A3BfC6ccDA1FF2fc:B8A33ACDfdfAeB79dc3fFdfD45e2E97a5c:8B1DdDbFABffd50bBBD76c8d7eB300D1a4bEB5Ac48Be42B13F1bAE55Edcb4c1432A84FAbD6B83a2bcEb3d1f57BeBfAa1e7AedE2B4DeC72e1A915e3Cd6:60FC0Fb295:d85Fd5a7d2E91B8dCAF9d8dcDCC4262E85132B826aFE7c29f2Cae679a92cF5bCaB09bcd39fDE6B50bD93701e7eBF9C00d9efE1bC2097281fCfF456a37B7c566315935D39D67E76e0:D7E7ECFBaF5B954Ab7342D0c14d92cA65aAECe1E7adC0aBcCB42BEf6a72cD18bcC61:DCafb5c516cA7cd2110dD7cB6Ee202633ddF76e4e4aCceBE0dDa2620Ae4fBCc7763c2730caBD77F4eCC4D14560Eab86d3C:ACA3C4badc44FBCdf4Ff031e13Eff1C1a8e337931:bA07CEfC2Ee5324a5f26e9eD3F2B1dEDC3ebC76D3C8dF8Af3A93aE374ceDCD6edF5F9CaC328fF8Abf0b9Aaa777bf2158c82D6fD26795:3Ce5Fa58364aa7aB8Afb4b8B4D9AF9329A63302C449D4BB5:16c8f543ae80a37784dFBD4eE91e7aB6F02b7D4a68b6edB8C3ebeF341279CeD17456BBdF12dace0DffCDeCFADCFaBbEfE5:37E9bdEde8E2Ee0EC5DE77acBBf6dFD8B6Df5497Ee52CaA3EBdF1C276ea2BEc7Ed401f'
                    ]
            )
        else :
            return ConnectivityCheckNic(
        )
        """

    def testConnectivityCheckNic(self):
        """Test ConnectivityCheckNic"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
