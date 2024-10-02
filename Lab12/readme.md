# Lab 12: Using Azure Resource Manager (ARM) Templates

## 1. Write an ARM template to deploy a multi-tier application.

```
{
  "$schema": "https://schema.management.azure.com/schemas/2019-04-01/deploymentTemplate.json#",
  "contentVersion": "1.0.0.0",
  "resources": [
    {
      "type": "Microsoft.Network/virtualNetworks",
      "apiVersion": "2020-06-01",
      "name": "myVnet",
      "location": "[resourceGroup().location]",
      "properties": {
        "addressSpace": {
          "addressPrefixes": [ "10.0.0.0/16" ]
        },
        "subnets": [
          {
            "name": "frontendSubnet",
            "properties": {
              "addressPrefix": "10.0.1.0/24"
            }
          },
          {
            "name": "backendSubnet",
            "properties": {
              "addressPrefix": "10.0.2.0/24"
            }
          }
        ]
      }
    },
    {
      "type": "Microsoft.Compute/virtualMachines",
      "apiVersion": "2020-06-01",
      "name": "frontendVM",
      "location": "[resourceGroup().location]",
      "properties": {
        "hardwareProfile": {
          "vmSize": "Standard_DS1_v2"
        },
        "osProfile": {
          "computerName": "frontendVM",
          "adminUsername": "azureuser",
          "adminPassword": "Password123!"
        },
        "networkProfile": {
          "networkInterfaces": [
            {
              "id": "[resourceId('Microsoft.Network/networkInterfaces', 'frontendNic')]"
            }
          ]
        }
      }
    },
    {
      "type": "Microsoft.Compute/virtualMachines",
      "apiVersion": "2020-06-01",
      "name": "backendVM",
      "location": "[resourceGroup().location]",
      "properties": {
        "hardwareProfile": {
          "vmSize": "Standard_DS1_v2"
        },
        "osProfile": {
          "computerName": "backendVM",
          "adminUsername": "azureuser",
          "adminPassword": "Password123!"
        },
        "networkProfile": {
          "networkInterfaces": [
            {
              "id": "[resourceId('Microsoft.Network/networkInterfaces', 'backendNic')]"
            }
          ]
        }
      }
    }
  ]
}

```

---

## 2. Parameterize the template for reusability.

```
{
  "$schema": "https://schema.management.azure.com/schemas/2019-04-01/deploymentTemplate.json#",
  "contentVersion": "1.0.0.0",
  "parameters": {
    "location": {
      "type": "string",
      "defaultValue": "West Europe",
      "metadata": {
        "description": "Location where the resources will be deployed"
      }
    },
    "vmSize": {
      "type": "string",
      "defaultValue": "Standard_DS1_v2",
      "metadata": {
        "description": "Size of the virtual machine"
      }
    }
  },
  "resources": [
    {
      "type": "Microsoft.Compute/virtualMachines",
      "apiVersion": "2020-06-01",
      "name": "frontendVM",
      "location": "[parameters('location')]",
      "properties": {
        "hardwareProfile": {
          "vmSize": "[parameters('vmSize')]"
        },
        "osProfile": {
          "computerName": "frontendVM",
          "adminUsername": "azureuser",
          "adminPassword": "Password123!"
        },
        "networkProfile": {
          "networkInterfaces": [
            {
              "id": "[resourceId('Microsoft.Network/networkInterfaces', 'frontendNic')]"
            }
          ]
        }
      }
    }
  ]
}
```

Fichier de paramètres
```
{
  "parameters": {
    "location": {
      "value": "East US"
    },
    "vmSize": {
      "value": "Standard_DS2_v2"
    }
  }
}
```

---

## 3. Deploy resources using the template via Azure CLI.

Créer un groupe de ressources:
```
az group create --name MyResourceGroup --location "East US"
```

Déployer le modèle ARM
```
az deployment group create \
  --resource-group MyResourceGroup \
  --template-file template.json \
  --parameters @parameters.json
```

---

## 4. Validate and troubleshoot deployment issues.

Valider le modèle ARM
```
az deployment group validate \
  --resource-group MyResourceGroup \
  --template-file template.json \
  --parameters @parameters.json
```

Afficher les détails des erreurs
```
az deployment group show \
  --resource-group MyResourceGroup \
  --name <deployment-name>
```

---

