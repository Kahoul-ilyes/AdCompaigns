import api from "@/lib/axios.ts";

export type AdCampaign = {
  id: number;
  name: string;
  description: string;
  start_date: string;
  end_date: string;
  budget: number;
  status: boolean;
}

export const fetchCampaigns = async () => {
  try {
    const response = await api.get('/adcampaigns')

    return await response.data;
  } catch (error) {
    console.error(error)
    throw error;
  }
}

export const createCampaign = async (adCampaign: AdCampaignForm) => {
  try {
    const response = await api.post('/adcampaigns', {
      ...adCampaign
    });

    return await response.data;
  } catch (error) {
    console.error(error)
    throw error;
  }
}

export const getCampaign = async (id: number) => {
  try {
    const response = await api.get(`/adcampaigns/${id}`);

    return await response.data;
  } catch (error) {
    console.error(error)
    throw error;
  }
}

export type AdCampaignForm = {
  name?: string;
  description?: string;
  start_date?: string;
  end_date?: string;
  budget?: number;
  status?: boolean;
}

export const updateCampaign = async (id: number, adCampaign: AdCampaignForm) => {
  try {
    const response = await api.patch(`/adcampaigns/${id}`, {
      ...adCampaign
    });

    return await response.data;
  } catch (error) {
    console.error(error)
    throw error;
  }
}

export const deleteCampaign = async (id: number) => {
  try {
    const response = await api.delete(`/adcampaigns/${id}`);

    return await response.data;
  } catch (error) {
    console.error(error)
    throw error;
  }
}

export const changeCampaignStatus = async (id: number, status: boolean) =>
  await updateCampaign(id, { status })
